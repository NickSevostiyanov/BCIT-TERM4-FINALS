# Terraform

## What you’ll learn
- Core Terraform workflow: `init → plan → apply → destroy`
- Project layout (`main.tf`, `variables.tf`, `outputs.tf`, `providers.tf`)
- Variables, outputs, state files
- Two examples on AWS:
  1) Create a versioned S3 bucket  
  2) Build a minimal VPC + public subnet + security group + EC2 instance

---

## Prerequisites

1. **Install Terraform**
   - macOS: `brew tap hashicorp/tap && brew install hashicorp/tap/terraform`
   - Windows: `choco install terraform`
   - Linux (Debian/Ubuntu): download from https://developer.hashicorp.com/terraform/downloads or use your package manager.

2. **Install & Configure AWS CLI**
   - Install: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
   - Configure credentials (creates `~/.aws/credentials` and `~/.aws/config`):
     ```bash
     aws configure
     # AWS Access Key ID [None]: AKIA....
     # AWS Secret Access Key [None]: ****************
     # Default region name [None]: us-east-1
     # Default output format [None]: json
     ```

3. **Permissions needed**
   - IAM user/role with permissions to create S3, EC2, VPC resources.

---

## Terraform Basics

- **Providers** connect Terraform to cloud platforms.  
- **Resources** describe infrastructure (e.g., `aws_s3_bucket`, `aws_instance`).  
- **Variables** parameterize code.  
- **Outputs** show values after apply.  
- **State** tracks what Terraform manages (`terraform.tfstate`).  
- **Workflow**
  - `terraform init` → download providers/modules
  - `terraform plan` → preview changes
  - `terraform apply` → create resources
  - `terraform destroy` → tear everything down

---

# Example 1: A Versioned S3 Bucket

### Folder layout
```
aws-s3-bucket/
├── main.tf
├── variables.tf
└── outputs.tf
```

### `main.tf`
```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_public_access_block" "this" {
  bucket                  = aws_s3_bucket.this.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

### `variables.tf`
```hcl
variable "aws_region" {
  description = "AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Globally unique S3 bucket name"
  type        = string
}
```

### `outputs.tf`
```hcl
output "bucket_name" {
  value = aws_s3_bucket.this.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.this.arn
}
```

### Run it
```bash
cd aws-s3-bucket

terraform init
terraform plan -var='bucket_name=your-unique-bucket-12345'
terraform apply -auto-approve -var='bucket_name=your-unique-bucket-12345'

aws s3 ls s3://your-unique-bucket-12345

terraform destroy -auto-approve -var='bucket_name=your-unique-bucket-12345'
```

---

# Example 2: Minimal VPC + Public Subnet + EC2

This creates a small VPC network and one EC2 instance you can SSH into.

### What it creates
- **VPC** (CIDR `10.0.0.0/16`)
- **Public Subnet** (CIDR `10.0.1.0/24`)
- **Internet Gateway** + **route**
- **Security Group** allowing SSH (port 22)
- **EC2 t2.micro** with a public IP

### Folder layout
```
aws-ec2-vpc/
├── main.tf
├── variables.tf
└── outputs.tf
```

### `main.tf`
```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = { Name = "${var.project}-vpc" }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
  tags   = { Name = "${var.project}-igw" }
}

resource "aws_subnet" "public_a" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = var.az
  tags = { Name = "${var.project}-public-a" }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  tags   = { Name = "${var.project}-public-rt" }
}

resource "aws_route" "internet_access" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.igw.id
}

resource "aws_route_table_association" "public_a" {
  subnet_id      = aws_subnet.public_a.id
  route_table_id = aws_route_table.public.id
}

resource "aws_security_group" "ssh" {
  name        = "${var.project}-ssh"
  description = "Allow SSH"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.ssh_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = { Name = "${var.project}-ssh" }
}

data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["137112412989"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_instance" "web" {
  ami                         = data.aws_ami.amazon_linux_2.id
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.public_a.id
  vpc_security_group_ids      = [aws_security_group.ssh.id]
  associate_public_ip_address = true
  key_name                    = var.key_name

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl enable httpd
              echo "Hello from Terraform on $(hostname)" > /var/www/html/index.html
              systemctl start httpd
              EOF

  tags = { Name = "${var.project}-ec2" }
}
```

### `variables.tf`
```hcl
variable "project" {
  description = "Project name used for tagging"
  type        = string
  default     = "tf-beginner"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "az" {
  description = "Availability Zone for the public subnet"
  type        = string
  default     = "us-east-1a"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "Name of an existing AWS EC2 key pair (.pem file)"
  type        = string
}

variable "ssh_cidr" {
  description = "CIDR allowed to SSH (use your IP/CIDR)"
  type        = string
  default     = "0.0.0.0/0"
}
```

### `outputs.tf`
```hcl
output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.web.public_ip
}

output "instance_http_url" {
  description = "HTTP URL for the demo web server"
  value       = "http://${aws_instance.web.public_ip}/"
}
```

### Run it
```bash
cd aws-ec2-vpc

terraform init
terraform plan -var="key_name=your-aws-keypair-name"
terraform apply -auto-approve -var="key_name=your-aws-keypair-name"

terraform output

ssh -i ~/path/to/your-keypair.pem ec2-user@$(terraform output -raw instance_public_ip)
curl $(terraform output -raw instance_http_url)

terraform destroy -auto-approve -var="key_name=your-aws-keypair-name"
```
