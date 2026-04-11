# ACIT4640 — IT System and Network Provisioning

## Course Details
| Field | Info |
|-------|------|
| **Course Code** | ACIT4640 |
| **Course Title** | IT System and Network Provisioning |
| **Instructor** | Dr. Motasem Aldiab — maldiab@bcit.ca |
| **Term** | Term 4, Set A, 2025–2026 |

---

## Grade Rubric

> ⚠️ Exact weights not confirmed — syllabus PDFs not machine-readable. Verify on D2L → Grades.

| # | Component | Est. Weight | Details |
|---|-----------|:-----------:|---------|
| 1 | **Labs** (weekly) | ~30% | Hands-on: AWS CLI, Terraform, Ansible, Packer |
| 2 | **Flipped Reviews** | ~10% | Weekly participation/review activities |
| 3 | **Quizzes** | ~10% | No dedicated quiz folder found — likely embedded in labs |
| 4 | **Final Exam** | ~50% | 90 min, closed book, pen/pencil |
| | **Total** | **~100%** | |

> **Minimum passing:** 50%. Aim for **70%+**
> **Check D2L** → ACIT4640 → Grades for exact weights.

---

## Logical Course Structure

| Week | Topic |
|------|-------|
| Intro | Install Ubuntu/Debian VM; set up DigitalOcean or AWS account |
| 1 | Cloud basics, lab week 1, reading review |
| 2 | Cloud CLI basics, lab 2 |
| 3 | **AWS CLI** — configure, EC2, IAM, S3, VPC, security groups, key pairs |
| 4 | **Infrastructure as Code** — Terraform intro (init/plan/apply/destroy), VPC/subnet/EC2 |
| 6 | **Ansible + Packer** — configuration management, image building |
| 9 | **Ansible on Ubuntu EC2** — inventory, playbooks, Nginx deploy |
| 10 | Advanced provisioning, lab |
| 11 | Lab continuation |
| 13–14 | Final prep |

---

## Final Exam Context

| Field | Info |
|-------|------|
| **Date** | Friday, April 24, 2026 |
| **Time** | 9:30 AM – 11:00 AM |
| **Duration** | 90 minutes |
| **Location** | DTC 825, Level 4 |
| **Open/Closed Book** | **Closed book** (assumed — same instructor as ACIT3495, bring ID + pen/pencil) |
| **Cheat Sheet** | Not allowed |
| **Exam Format** | Written — likely short answer + fill-in commands + conceptual questions |

> **Bring:** Student ID + pen or pencil

---

## Course Overview

**AWS CLI:** Unified CLI tool to manage AWS services. Configure profiles (`~/.aws/credentials`), manage EC2 (key pairs, security groups, launch/stop/terminate), IAM (users, groups, policies, access keys), S3 (list, copy, sync), VPC networking.

**Terraform (IaC):** Declarative infrastructure as code. Core workflow: `init → plan → apply → destroy`. Project files: `main.tf`, `variables.tf`, `outputs.tf`, `providers.tf`. State tracked in `terraform.tfstate`.

**Ansible:** Agentless configuration management tool. Uses SSH to configure remote hosts. Key files: `inventory` (hosts), `ansible.cfg` (settings), playbooks (YAML). Common modules: `ping`, `apt`, `service`, `copy`, `template`.

**Packer:** Tool for building machine images (AMIs). Defines image builds as code in `.pkr.hcl` files. Builds on top of a source AMI, runs provisioners (scripts/Ansible), outputs a new AMI.

**Networking Concepts:** VPC (Virtual Private Cloud), subnets (public/private), Internet Gateway, route tables, security groups (stateful firewall), CIDR notation, SSH key pairs, public IPs.
