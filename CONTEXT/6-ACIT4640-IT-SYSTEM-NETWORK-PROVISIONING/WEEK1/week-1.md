# ACIT 4640 Week 1

## Learning outcomes and topics

- Introductions
	- tools overviews
	- important general terminology
	- development environment setup

## course outline

### Office hours

Please make office hours appointments at least 24 hours in advance.

When you make an appoint include information about what you would like to discuss. 

see your D2L section for more information about office hours

### evaluation criteria


| Criteria                | %   | Comments                                          |
| ----------------------- | --- | ------------------------------------------------- |
| Flipped material review | 10  | To be done in class<br>10 reviews weighted evenly |
| Labs                    | 15  | To be done in class<br>10 labs weighted evenly    |
| Tests                   | 30  | 2 tests, 15% each                                 |
| Final exam              | 45  | Comprehensive                                     |

### Tests

Tests will be done during regular class time. More information about the tests will be provided in class later in the term.

### Flipped material reviews and Labs

These are both in-class activities 

These are both pass/fail activities.

The flipped material reviews will help you better understand the conceptual information, and improve your general understanding of the topics covered in the course.

The labs will help you develop practical skills related to the topics covered in the course.
 
### Course notes

Course note are provided as markdown documents via GitLab. You can incorporate these notes into your own notes (recommended) or just view them on GitLab.

### Flipped learning material

Each week material will be provided in these notes. Please complete this material before the following weeks class.

The complete course outline is available [here](https://www.bcit.ca/programs/computer-information-technology-diploma-full-time-5540dipma/#courses).
## course tools overview

### AWS as a cloud service provider

- AWS is still the largest cloud service provider
- You have previous experience with AWS

Ideally the course could be cloud service provider agnostic. 

### Terraform/OpenTofu

[Terraform](https://www.terraform.io/) is an [IaC](https://www.ibm.com/think/topics/infrastructure-as-code) tool used to provision and manage resources in any cloud or data center. We will use Terraform to provision resources in AWS. 

Rather than creating an EC2 instance and all of the necessary networking in the AWS console we can configure it in plain text files using Terraform. These plain text files can be shared with a team using existing tools like Git.

On August 10th 2023 HashiCorp changed the license of some of their products from MPL 2.0 to BSL v1.1. As students learning this technology this won't impact you. It does however impact organisation using Terraform, particularly third party service providers.

[OpenTofu](https://opentofu.org/) Was forked from Terraform because of this license change. When OpenTofu was introduced it was a drop-in replacement for Terraform. Both projects are still very similar and learning one will make it relatively easy to pick up the other

#### Other alternatives

AWS has [CloudFormation](https://docs.aws.amazon.com/cloudformation/) and [CDK](https://aws.amazon.com/cdk/) These are both AWS specific solutions. Most of the teams I have worked on have used more than one cloud service provider as well as on-premise infrastructure. Using one tool to manage multiple cloud service providers and your own infrastructure makes things easier.

[Pulumi](https://www.pulumi.com/) is a tool similar to Terraform in that it is cloud agnostic, but instead of using a [DSL](https://www.jetbrains.com/mps/concepts/domain-specific-languages/), Pulumi configuration is written in one of a handful of popular programming languages.

### Packer

Where Terraform is generally used to create resources, networking, a database cluster, virtual machines... Packer is used to create images that can run in VMs or containers.

Packer can be used to create "identical" machine images for different platforms from the same packer template. So, if we wanted to run our application on AWS, GCP, DO and our on own servers, we could create images that contain our application for all of those platforms from the same source files.

After creating an image in Packer you would use Terraform to deploy that image in a VM.

### Ansible

Although Terraform and Ansible can both be used to deploy and manage infrastructure, generally Terraform is used to deploy infrastructure and [Ansible](https://www.ansible.com/) is used to manage some of that infrastructure. Ansible can be used to perform actions such as installing software or copying files to a server. Ansible is also often used in conjunction with [Packer](https://www.packer.io/), to build images that already contain application resources.

**Reference:**

- [What is an image builder](https://www.redhat.com/en/topics/linux/what-is-an-image-builder)
- [Terraform](https://www.terraform.io/)
- [Packer](https://www.packer.io/)
- [Ansible](https://docs.ansible.com/ansible/latest/getting_started/index.html)

## important terminology

### Infrastructure

Infrastructure is the components that make up a system used to deploy and maintain applications and services. This includes things like:

- Virtual Machines
- Load Balancers
- Networks

### Provisioning

> Provisioning is the process of creating and setting up IT infrastructure, and includes the steps required to manage user and system access to various resources. Provisioning is an early stage in the deployment of servers, applications, network components, storage, edge devices, and more.
> 
> - [RedHat What is Provisioning](https://www.redhat.com/en/topics/automation/what-is-provisioning)

### Management

> Configuration management is a process for maintaining computer systems, servers, applications, network devices, and other IT components in a desired state. It’s a way to help ensure that a system performs as expected, even after many changes are made over time.
> 
> - [RedHat What is configuration management](https://www.redhat.com/en/topics/automation/what-is-configuration-management)

### Infrastructure as Code (IaC)

IaC is Infrastructure management provision using code instead of a manual process. Plain text files contain instructions to provision and manage infrastructure that can be share with a team using version control systems.

IaC has some of the following bennefits:

- Reproducible
- Easier to scale.
- Easier to maintain

IaC tools generally use one of two approaches:

- Declarative
- Imperative

> A declarative approach defines the desired state of the system, including what resources you need and any properties they should have, and an IaC tool will configure it for you.
> 
> An imperative approach instead defines the specific commands needed to achieve the desired configuration, and those commands then need to be executed in the correct order.
> 
> - [RedHat What is Infrastructure as Code (IaC)?](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac)

**Reference:**

- [IBM What is Infrastructure as Code (IaC)](https://www.ibm.com/topics/infrastructure-as-code)

### DevOps

![devops diagram](../attach/devops.png)


DevOps is practice of using a developer mindset and developer workflow to perform operations tasks. DevOps allows an operations team to perform tasks faster and to make those tasks more reproducible. DevOps also allows a team to experiment and perform more tests.

**Reference:**

- [AWS What is DevOps](https://aws.amazon.com/devops/what-is-devops/)
- [IBM What is DevOps](https://www.ibm.com/topics/devops)

## local Linux development environment set up

Some of the tools that we are going to use this term have; limited MacOS and WIndows support, because of this you will need to have a Linux environment to do the labs in this course.

### Specifics

Please create a Debian Linux development environment using one of the methods below. Your development environment should run either Debian "trixie" 13, or Debian "forky" 14.

Maintaining your development environment is your responsibility. There will not be a lot of class time devoted to this.

You can use any of the following:
- [WSL](https://learn.microsoft.com/en-us/windows/wsl/) (Windows Subsystem for Linux). If you are running Windows 10 or 11
- A VM using a tool like VirtualBox
- Run a container using a tool like [Podman](https://podman.io/) or [Docker](https://www.docker.com/)
- Use a cloud dev environment
	- Either using an exiting tool purpose built for this like [Codespaces](https://github.com/features/codespaces)
	- Or maintain your own in AWS, DigitalOcean...
- Install a Linux distro on your laptop (either dual boot or as your only OS)
	- If you have compatible hardware this is probably the easiest option.

[WSL set up](./WSL-Resources.md) resource.

## flipped learning material

The flipped learning material should be reviewed before the next class.

- [Bash variables, environment variables and command substitution](https://docs.rockylinux.org/books/learning_bash/02-using-variables/)
- [Bash Heredoc](https://linuxize.com/post/bash-heredoc/)
- [`systemctl` commands](https://www.linode.com/docs/guides/introduction-to-systemctl/)
- [What Is SSH: Understanding Encryption, Ports and Connection](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)

Starting next week everyone should bring a **pen or pencil and paper** to class for in class activities.
