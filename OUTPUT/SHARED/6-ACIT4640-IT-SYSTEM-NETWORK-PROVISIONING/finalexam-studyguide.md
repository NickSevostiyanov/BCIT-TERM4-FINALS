# ACIT4640 — Final Exam Study Guide
> 90 min | Closed Book | Pen/pencil + ID | DTC 825 | Friday April 24, 2026 @ 9:30 AM
> **Topics: AWS CLI, Terraform, Ansible, Packer, VPC/Networking**

---

## 1. AWS CLI

### Setup & Config
```bash
aws configure                    # set up default profile
aws configure --profile dev      # named profile
aws sts get-caller-identity      # verify who you're logged in as
aws configure list               # show current config
```
- Stores to: `~/.aws/credentials` (keys) and `~/.aws/config` (region/format)
- Output formats: `json` (default), `table`, `text`
- Filter output: `--query` uses JMESPath syntax
- `--dry-run` — validates permissions WITHOUT making changes
- `--no-paginate` — disables pagination on list commands

### EC2 — Full Workflow
```bash
# Key pair
aws ec2 create-key-pair --key-name demo-key --query 'KeyMaterial' --output text > demo-key.pem
chmod 600 demo-key.pem

# Security Group
SG_ID=$(aws ec2 create-security-group --group-name web-sg --description "web" --vpc-id VPC_ID --query 'GroupId' --output text)
MYIP=$(curl -s https://checkip.amazonaws.com)
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr ${MYIP}/32
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 80 --cidr 0.0.0.0/0

# Launch EC2
aws ec2 run-instances --image-id AMI_ID --instance-type t2.micro \
  --key-name demo-key --security-group-ids $SG_ID --subnet-id SUBNET_ID \
  --associate-public-ip-address --count 1

# Start / Stop / Terminate
aws ec2 stop-instances --instance-ids INSTANCE_ID
aws ec2 start-instances --instance-ids INSTANCE_ID
aws ec2 terminate-instances --instance-ids INSTANCE_ID

# Wait for state
aws ec2 wait instance-running --instance-ids INSTANCE_ID

# SSH in
ssh -i demo-key.pem ec2-user@PUBLIC_IP      # Amazon Linux
ssh -i demo-key.pem ubuntu@PUBLIC_IP        # Ubuntu
```

### VPC Networking
```bash
# Create VPC
VPC_ID=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query 'Vpc.VpcId' --output text)

# Subnet
SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a --query 'Subnet.SubnetId' --output text)
aws ec2 modify-subnet-attribute --subnet-id $SUBNET_ID --map-public-ip-on-launch

# Internet Gateway
IGW_ID=$(aws ec2 create-internet-gateway --query 'InternetGateway.InternetGatewayId' --output text)
aws ec2 attach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID

# Route Table
RT_ID=$(aws ec2 create-route-table --vpc-id $VPC_ID --query 'RouteTable.RouteTableId' --output text)
aws ec2 create-route --route-table-id $RT_ID --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID
aws ec2 associate-route-table --route-table-id $RT_ID --subnet-id $SUBNET_ID
```

### IAM
```bash
aws iam list-users
aws iam create-group --group-name Admins
aws iam attach-group-policy --group-name Admins --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws iam add-user-to-group --group-name Admins --user-name USERNAME
aws iam create-access-key --user-name USERNAME
aws iam update-access-key --user-name USERNAME --access-key-id AKIA... --status Inactive
aws iam delete-access-key --user-name USERNAME --access-key-id AKIA...
```

### S3
```bash
aws s3 ls                                              # list buckets
aws s3 ls s3://MY-BUCKET/ --recursive --human-readable
aws s3 cp file.txt s3://MY-BUCKET/
aws s3 sync ./site s3://MY-BUCKET/site/
aws s3 mb s3://new-bucket-name
```

---

## 2. Terraform (IaC)

### Core Workflow
| Command | What it does |
|---------|-------------|
| `terraform init` | Download providers/modules — run first |
| `terraform plan` | Preview changes (dry run) — shows what WILL happen |
| `terraform apply` | Create/update resources |
| `terraform apply -auto-approve` | Apply without interactive confirmation |
| `terraform destroy` | Tear down all managed resources |
| `terraform output` | Show output values |
| `terraform show` | Show current state |

### Project File Structure
```
project/
├── main.tf          # resources + provider block
├── variables.tf     # input variable definitions
├── outputs.tf       # output value definitions
└── providers.tf     # provider config (optional, can be in main.tf)
```
- **State** stored in `terraform.tfstate` — DO NOT delete
- **`terraform.tfstate`** tracks what Terraform manages

### Key HCL Syntax
```hcl
# Provider
provider "aws" {
  region = var.aws_region
}

# Resource
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type
  key_name      = var.key_name
  tags = { Name = "my-ec2" }
}

# Variable definition (variables.tf)
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

# Output (outputs.tf)
output "public_ip" {
  value = aws_instance.web.public_ip
}

# Data source (look up existing resource)
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}
```

### VPC + EC2 Resource Chain (exam-style)
```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id    # reference other resource
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
}
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
}
resource "aws_security_group" "ssh" {
  vpc_id = aws_vpc.main.id
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0; to_port = 0; protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

### Pass variables
```bash
terraform plan -var="key_name=my-keypair"
terraform apply -var="key_name=my-keypair" -var="instance_type=t2.micro"
```

---

## 3. Ansible

### What is Ansible?
- **Agentless** configuration management — uses SSH, no agent installed on targets
- **Push-based** — control node pushes config to managed nodes
- Written in Python; playbooks in YAML

### Key Files
```ini
# inventory (hosts file)
[web]
192.168.1.10 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem
192.168.1.11 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem

[db]
192.168.1.20 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem
```

```ini
# ansible.cfg
[defaults]
inventory = ./inventory
host_key_checking = False
retry_files_enabled = False
```

### Key Commands
```bash
ansible all -m ping                          # test connectivity
ansible web -m ping                          # ping web group only
ansible all -m command -a "uptime"           # run command
ansible-playbook playbook.yml                # run a playbook
ansible-playbook playbook.yml --check        # dry run
ansible-playbook playbook.yml -v             # verbose
```

### Playbook Structure
```yaml
---
- name: Configure web servers
  hosts: web
  become: yes          # sudo

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install Nginx
      apt:
        name: nginx
        state: present

    - name: Start and enable Nginx
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Deploy homepage
      copy:
        content: "<h1>Hello from Ansible!</h1>"
        dest: /var/www/html/index.html
        mode: '0644'
```

### Common Modules
| Module | Purpose |
|--------|---------|
| `ping` | Test connectivity (returns "pong") |
| `apt` | Manage packages (Ubuntu/Debian) |
| `yum` | Manage packages (RHEL/Amazon Linux) |
| `service` | Start/stop/enable services |
| `copy` | Copy files to remote |
| `template` | Deploy Jinja2 templates |
| `command` | Run shell commands (no shell features) |
| `shell` | Run shell commands (with pipes, redirects) |
| `file` | Manage files/dirs/permissions |
| `user` | Manage user accounts |

---

## 4. Packer

### What is Packer?
- Builds **machine images** (AMIs) from code
- Defines build process in `.pkr.hcl` (HCL) or JSON
- Builds on a source AMI → runs provisioners → outputs a new AMI

### Key Concepts
```hcl
# web-front.pkr.hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = "~> 1"
    }
  }
}

source "amazon-ebs" "ubuntu" {
  ami_name      = "web-front-{{timestamp}}"
  instance_type = "t2.micro"
  region        = "us-east-1"
  source_ami_filter {
    filters = {
      name                = "ubuntu/images/*ubuntu-focal-20.04-amd64-server-*"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners      = ["099720109477"]  # Canonical
  }
  ssh_username = "ubuntu"
}

build {
  sources = ["source.amazon-ebs.ubuntu"]

  provisioner "shell" {
    script = "scripts/install-nginx"
  }

  provisioner "file" {
    source      = "files/index.html"
    destination = "/var/www/html/index.html"
  }
}
```

### Packer Commands
```bash
packer init .           # download plugins
packer validate .       # check HCL syntax
packer build .          # build the image
```

---

## 5. Networking Concepts (VPC)

| Concept | Definition |
|---------|-----------|
| **VPC** | Virtual Private Cloud — isolated network in AWS |
| **Subnet** | Subdivision of VPC CIDR; public (has IGW route) or private |
| **CIDR** | IP range notation: `10.0.0.0/16` = 65,536 IPs; `/24` = 256 IPs |
| **Internet Gateway (IGW)** | Allows VPC resources to reach internet |
| **Route Table** | Rules directing network traffic; must associate with subnet |
| **Security Group** | Stateful firewall — controls inbound/outbound at instance level |
| **Key Pair** | SSH public/private key for EC2 access; `.pem` = private key |
| **AMI** | Amazon Machine Image — blueprint for EC2 instance |
| **t2.micro** | Free-tier eligible instance type |

### CIDR Quick Reference
| CIDR | Hosts |
|------|-------|
| /16 | 65,536 |
| /24 | 256 |
| /32 | 1 (single IP) |
| 0.0.0.0/0 | All IPs (anywhere) |

### SSH Commands
```bash
chmod 600 mykey.pem                          # required before SSH
ssh -i mykey.pem ec2-user@PUBLIC_IP          # Amazon Linux
ssh -i mykey.pem ubuntu@PUBLIC_IP            # Ubuntu
ssh -i mykey.pem -p 22 user@IP               # explicit port
```

---

## 6. IaC Concepts (Infrastructure as Code)

| Concept | Meaning |
|---------|---------|
| **IaC** | Define infrastructure in code files (version-controlled, repeatable) |
| **Declarative** | Describe the DESIRED STATE — tool figures out how (Terraform) |
| **Imperative** | Describe the STEPS to take — you specify how (scripts, AWS CLI) |
| **Idempotent** | Running the same operation multiple times = same result |
| **Provisioning** | Creating/configuring infrastructure (VMs, networks) |
| **Configuration Management** | Installing/configuring software on existing infra (Ansible) |
| **Image Building** | Baking software into a reusable machine image (Packer) |

### Tool Comparison
| Tool | Type | What it does |
|------|------|-------------|
| **AWS CLI** | Imperative | Manage AWS via commands/scripts |
| **Terraform** | Declarative IaC | Provision infrastructure |
| **Ansible** | Config Management | Configure software on existing servers |
| **Packer** | Image Building | Build AMIs/images from code |

---

## 7. Quick-Fire Facts

| Statement | Answer |
|-----------|--------|
| `terraform plan` creates resources | **NO** — just previews them |
| `terraform init` must be run before anything else | **YES** |
| Ansible requires an agent on target hosts | **NO** — agentless (uses SSH) |
| Packer creates running EC2 instances | **NO** — creates AMIs (images) |
| `chmod 600` on .pem file is required for SSH | **YES** |
| Default SSH user for Amazon Linux = `ubuntu` | **NO** — `ec2-user` |
| Default SSH user for Ubuntu AMIs = `ubuntu` | **YES** |
| Security groups are stateful | **YES** — return traffic auto-allowed |
| `0.0.0.0/0` CIDR means all IPs | **YES** |
| Terraform state file = `terraform.tfstate` | **YES** |
| `--dry-run` in AWS CLI modifies resources | **NO** — only checks permissions |
| Ansible `ping` module tests if host is reachable | **YES** (returns "pong") |
| `become: yes` in Ansible = run as sudo | **YES** |
| Route table must be associated with subnet | **YES** |
| Internet Gateway needed for public subnet | **YES** |
