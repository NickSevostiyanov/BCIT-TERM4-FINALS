# AWS CLI



---

## Slides

### Slide 1 — Title & Goal
- **Topic:** AWS CLI — Concepts & Hands‑On
- **Goal:** Learn core commands and run a minimal EC2 end‑to‑end.
- **Plan:** Configure CLI → list IAM/S3 → create key → SG → launch EC2.

---

### Slide 2 — What is AWS CLI?
- Unified command‑line tool to manage AWS services.
- Great for automation and scripting.
- Pattern: `aws [options] <service> <operation> [params]`
```bash
aws help
aws ec2 help
```

---

### Slide 3 — Install & Version Check
- Linux/macOS (pip): `python3 -m pip install --upgrade awscli`
- macOS (Homebrew): `brew install awscli`
- Windows: use the official MSI installer.
```bash
aws --version
```

---

### Slide 4 — Configure Your First Profile
- Stores credentials, default region, and output format.
- Creates `~/.aws/credentials` and `~/.aws/config`.
- Use named profiles for multiple accounts.
```bash
aws configure               # default profile
aws configure --profile dev # named profile
```

---

### Slide 5 — Where Config Lives
- **Credentials:** `~/.aws/credentials`
- **Config:** `~/.aws/config`
- Use a profile explicitly when needed.
```bash
aws sts get-caller-identity --profile dev
```

---

### Slide 6 — Command Structure & Pagination
- `aws SERVICE OPERATION [--flags]`
- Many list operations paginate; disable if needed.
```bash
aws ec2 describe-instances --no-paginate
```

---

### Slide 7 — Output Formats & --query (JMESPath)
- Formats: `json` (default), `table`, `text`
- Filter client‑side with `--query` for concise output
```bash
aws ec2 describe-instances   --output table   --query "Reservations[].Instances[].{Id:InstanceId,Type:InstanceType,State:State.Name}"
```

---

### Slide 8 — Shell Completion & Help
- Enable autocompletion (path may vary).
- Use service/operation-specific help.
```bash
complete -C '/usr/bin/aws_completer' aws
aws s3 help
aws ec2 run-instances help
```

---

### Slide 9 — S3 Basics (List & Copy)
- List buckets/objects; recurse and summarize.
- Copy files or sync directories.
```bash
aws s3 ls
aws s3 ls s3://MY-BUCKET/ --recursive --human-readable --summarize
aws s3 cp file.txt s3://MY-BUCKET/
aws s3 sync ./site s3://MY-BUCKET/site/
```

---

### Slide 10 — IAM: Users at a Glance
- List users and inspect identity/keys.
```bash
aws iam list-users --no-paginate
aws iam get-user
aws iam list-access-keys --user-name USERNAME
```

---

### Slide 11 — IAM: Create & Rotate Access Keys
- Create, check last used, deactivate, delete.
- Follow least‑privilege and rotation best practices.
```bash
aws iam create-access-key --user-name USERNAME
aws iam get-access-key-last-used --access-key-id AKIA...EXAMPLE
aws iam update-access-key --user-name USERNAME --access-key-id AKIA... --status Inactive
aws iam delete-access-key --user-name USERNAME --access-key-id AKIA...
```

---

### Slide 12 — IAM: Groups & Policies (Admin Example)
- Attach managed policies to groups; add users to groups.
- **Prod tip:** Prefer least‑privilege over admin.
```bash
aws iam create-group --group-name FullAdmins
aws iam attach-group-policy   --group-name FullAdmins   --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws iam add-user-to-group --group-name FullAdmins --user-name USERNAME
```

---

### Slide 13 — EC2 Concepts (Fast Map)
- **Key pair** (SSH), **Security Group** (firewall), **AMI** (image), **Instance Type**.
- **VPC/Subnet** for networking.

---

### Slide 14 — EC2: Key Pairs
- List, create, import; protect private keys.
```bash
aws ec2 describe-key-pairs
aws ec2 create-key-pair --key-name demo-key --query 'KeyMaterial' --output text > demo-key.pem
chmod 600 demo-key.pem
# Or import an existing public key
aws ec2 import-key-pair --key-name demo-key --public-key-material file://~/.ssh/id_rsa.pub
```

---

### Slide 15 — EC2: Security Groups
- Create SG and open only needed ports.
- Lock SSH to your IP.
```bash
aws ec2 create-security-group   --group-name web-access --description "web access" --vpc-id VPC_ID
MYIP=$(curl -s https://checkip.amazonaws.com)
aws ec2 authorize-security-group-ingress   --group-id SG_ID --protocol tcp --port 22 --cidr ${MYIP}/32
aws ec2 authorize-security-group-ingress   --group-id SG_ID --protocol tcp --port 80 --cidr 0.0.0.0/0
```

---

### Slide 16 — EC2: AMI Lookup (Quick Filter)
- Find a recent Amazon Linux 2 AMI (x86_64).
```bash
aws ec2 describe-images   --owners amazon   --filters 'Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2' 'Name=state,Values=available'   --query 'Images[].{Name:Name,Id:ImageId}' --output table
```

---

### Slide 17 — EC2: Dry‑Run a Launch
- Validate permissions without changing state.
```bash
aws ec2 run-instances   --image-id AMI_ID --instance-type t2.micro   --key-name demo-key --security-group-ids SG_ID --subnet-id SUBNET_ID   --associate-public-ip-address --count 1 --dry-run
```

---

### Slide 18 — EC2: Launch + Tag (jq needed)
- Launch an instance and add a Name tag.
- `jq` parses JSON locally.
```bash
INSTANCE_JSON=$(aws ec2 run-instances   --image-id AMI_ID --instance-type t2.micro   --key-name demo-key --security-group-ids SG_ID --subnet-id SUBNET_ID   --associate-public-ip-address --count 1)
INSTANCE_ID=$(echo "$INSTANCE_JSON" | jq -r '.Instances[0].InstanceId')
aws ec2 create-tags --resources "$INSTANCE_ID" --tags Key=Name,Value=demo-ec2
```

---

### Slide 19 — EC2: Describe Instances (Readable)
- Output as table; select key fields.
```bash
aws ec2 describe-instances --output table   --query "Reservations[].Instances[].{Id:InstanceId,Name:Tags[?Key=='Name'].Value|[0],State:State.Name,IP:PublicIpAddress,Type:InstanceType}"
```

---

### Slide 20 — EC2: Start / Stop / Terminate
- Start/stop for savings; terminate to end billing.
- Volumes may persist if not delete‑on‑termination.
```bash
aws ec2 stop-instances --instance-ids INSTANCE_ID
aws ec2 start-instances --instance-ids INSTANCE_ID
aws ec2 terminate-instances --instance-ids INSTANCE_ID
```

---

### Slide 21 — Tagging Resources
- Use tags for ownership, environment, and cost reporting.
```bash
aws ec2 create-tags --resources RESOURCE_ID --tags Key=env,Value=dev Key=owner,Value=me
aws ec2 describe-tags --filters Name=resource-id,Values=RESOURCE_ID
```

---

### Slide 22 — CloudWatch Logs: Quick Start
- Create a log group/stream; list groups.
```bash
aws logs create-log-group --log-group-name MyGroup
aws logs create-log-stream --log-group-name MyGroup --log-stream-name app
aws logs describe-log-groups --log-group-name-prefix My
```

---

### Slide 23 — CloudTrail: Basic Trail (Correct API)
- Create an S3 bucket, trail, and start logging.
```bash
aws s3 mb s3://MY-UNIQUE-TRAIL-BUCKET
aws cloudtrail create-trail --name acct-trail --s3-bucket-name MY-UNIQUE-TRAIL-BUCKET
aws cloudtrail start-logging --name acct-trail
aws cloudtrail get-trail-status --name acct-trail
```

---

### Slide 24 — Safer Listing with --query
- Return only the columns you need.
```bash
aws iam list-users --output table   --query 'Users[].{Name:UserName,Created:CreateDate}'
```

---

### Slide 25 — Filter IDs for Scripting
- Extract IDs for pipelines and loops.
```bash
aws ec2 describe-instances   --filters Name=instance-state-name,Values=running   --query 'Reservations[].Instances[].InstanceId' --output text
```

---

### Slide 26 — Regions & Profiles On Demand
- Override region and profile per command.
```bash
aws ec2 describe-vpcs --region us-west-2
aws s3 ls --profile dev
```

---

### Slide 27 — Dry‑Run & Exit Codes
- Use `--dry-run` to check permissions.
- Non‑zero exit → failure (use in scripts).
```bash
aws ec2 terminate-instances --instance-ids i-123 --dry-run || echo "Would fail (or not allowed)"
```

---

### Slide 28 — Handy Bash One‑Liners
- Combine with `--output text` for quick pipelines.
```bash
# print first 5 lines of a file
head -n 5 README.md
# get only column 2 from tab-separated text
cut -f 2 data.tsv
```

---

### Slide 29 — Common Pitfalls (Fast)
- Avoid using root credentials; use IAM users/roles.
- Lock SSH to your IP; avoid open `0.0.0.0/0` on port 22.
- Set a default region; use `--query` + `--output table` for readability.

---

### Slide 30 — Cleanup Checklist
- Terminate test EC2; delete unattached EBS.
- Remove temporary security groups and key pairs.
- Delete unused log groups & S3 buckets.
```bash
aws ec2 describe-instances --query 'Reservations[].Instances[].State.Name' --output text
```

---

## Hands‑On Story — Key Pair → VPC → Security Group → EC2 → SSH

> Goal: Create a key pair, minimal VPC pieces, a security group, launch an EC2 instance, and SSH into it. Replace ALL_CAPS values. Region used in examples: `us-west-2`.

### 0) Prerequisites
- AWS CLI installed and configured (e.g., `default` profile).
- Tools: `jq` (optional), `ssh`.
```bash
aws sts get-caller-identity
aws configure list
```

### 1) Create or Import a Key Pair
```bash
# Option A: Create on AWS, save private key locally
aws ec2 create-key-pair --key-name demo-key   --query 'KeyMaterial' --output text > demo-key.pem
chmod 600 demo-key.pem

# Option B: Import your existing public key
# aws ec2 import-key-pair --key-name demo-key --public-key-material file://~/.ssh/id_rsa.pub
```

### 2) Create a Minimal VPC Setup
```bash
# 2.1 Create VPC (10.0.0.0/16)
VPC_ID=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16   --query 'Vpc.VpcId' --output text)
aws ec2 create-tags --resources "$VPC_ID" --tags Key=Name,Value=demo-vpc

# 2.2 Create a public subnet (10.0.1.0/24) in us-east-1a
SUBNET_ID=$(aws ec2 create-subnet --vpc-id "$VPC_ID" --cidr-block 10.0.1.0/24   --availability-zone us-east-1a --query 'Subnet.SubnetId' --output text)
aws ec2 modify-subnet-attribute --subnet-id "$SUBNET_ID" --map-public-ip-on-launch

# 2.3 Internet Gateway + attach to VPC
IGW_ID=$(aws ec2 create-internet-gateway --query 'InternetGateway.InternetGatewayId' --output text)
aws ec2 attach-internet-gateway --internet-gateway-id "$IGW_ID" --vpc-id "$VPC_ID"

# 2.4 Route table: route all internet traffic via IGW
RT_ID=$(aws ec2 create-route-table --vpc-id "$VPC_ID" --query 'RouteTable.RouteTableId' --output text)
aws ec2 create-route --route-table-id "$RT_ID" --destination-cidr-block 0.0.0.0/0 --gateway-id "$IGW_ID"
aws ec2 associate-route-table --route-table-id "$RT_ID" --subnet-id "$SUBNET_ID"
```

### 3) Security Group (SSH from your IP + HTTP for tests)
```bash
SG_ID=$(aws ec2 create-security-group   --group-name demo-sg --description "demo sg" --vpc-id "$VPC_ID"   --query 'GroupId' --output text)
MYIP=$(curl -s https://checkip.amazonaws.com)
aws ec2 authorize-security-group-ingress --group-id "$SG_ID" --protocol tcp --port 22 --cidr ${MYIP}/32
aws ec2 authorize-security-group-ingress --group-id "$SG_ID" --protocol tcp --port 80 --cidr 0.0.0.0/0
```

### 4) Find an AMI & Launch EC2
```bash
# 4.1 Find a recent Amazon Linux 2 AMI (x86_64)
AMI_ID=$(aws ec2 describe-images   --owners amazon   --filters 'Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2' 'Name=state,Values=available'   --query 'Images | sort_by(@,&CreationDate) | [-1].ImageId' --output text)

echo "Using AMI: $AMI_ID"

# 4.2 Launch a t2.micro in the public subnet, with public IP
RUN_JSON=$(aws ec2 run-instances   --image-id "$AMI_ID" --instance-type t2.micro   --key-name demo-key --security-group-ids "$SG_ID" --subnet-id "$SUBNET_ID"   --associate-public-ip-address --count 1)
INSTANCE_ID=$(echo "$RUN_JSON" | jq -r '.Instances[0].InstanceId')
aws ec2 create-tags --resources "$INSTANCE_ID" --tags Key=Name,Value=demo-ec2

# 4.3 Wait for running + grab public IP
aws ec2 wait instance-running --instance-ids "$INSTANCE_ID"
PUBLIC_IP=$(aws ec2 describe-instances --instance-ids "$INSTANCE_ID"   --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)

echo "EC2 is up at: $PUBLIC_IP"
```

### 5) SSH In
```bash
ssh -i demo-key.pem ec2-user@${PUBLIC_IP}
# (On Ubuntu AMIs the user is often 'ubuntu')
```

### 6) Verify & Cleanup (Optional)
```bash
# verify
uname -a && whoami && curl -I http://169.254.169.254/latest/meta-data/

# cleanup
aws ec2 terminate-instances --instance-ids "$INSTANCE_ID"
aws ec2 wait instance-terminated --instance-ids "$INSTANCE_ID"
aws ec2 delete-security-group --group-id "$SG_ID"
aws ec2 detach-internet-gateway --internet-gateway-id "$IGW_ID" --vpc-id "$VPC_ID"
aws ec2 delete-internet-gateway --internet-gateway-id "$IGW_ID"
aws ec2 delete-subnet --subnet-id "$SUBNET_ID"
aws ec2 delete-route-table --route-table-id "$RT_ID"
aws ec2 delete-vpc --vpc-id "$VPC_ID"
# optionally: aws ec2 delete-key-pair --key-name demo-key; rm -f demo-key.pem
```

