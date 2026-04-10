# Ansible with AWS EC2 Ubuntu Instances and `.pem` Key Files

This guide shows how to use **Ansible** from your local machine to connect to and configure **Ubuntu EC2 instances on AWS** using an **EC2 `.pem` private key file**.

It is written specifically for the common AWS setup where:
- the target servers are **EC2 instances**
- SSH access uses a downloaded **`.pem` key pair file**
- the default SSH user for Ubuntu is **`ubuntu`**

Source adapted from the uploaded guide. fileciteturn0file0

---

## Prerequisites

Before starting, make sure you have:

- An **AWS account** with permission to create and manage EC2 instances.
- **Two Ubuntu EC2 instances** running in AWS.
- A downloaded AWS key pair file such as:
  - `mykey.pem`
  - stored in a safe location such as `~/.ssh/mykey.pem`
- The **public IPv4 addresses** or **public DNS names** of your EC2 instances.
- A security group that allows:
  - **SSH (port 22)** from your IP address
  - **HTTP (port 80)** from anywhere if you want to test Nginx in the browser

---

## Step 1: Launch Ubuntu EC2 Instances in AWS

In the **AWS Console**:

1. Go to **EC2**.
2. Click **Launch instances**.
3. Choose:
   - **AMI:** Ubuntu Server 22.04 LTS or Ubuntu Server 24.04 LTS
   - **Instance type:** `t2.micro` or `t3.micro`
4. Under **Key pair**, either:
   - select an existing key pair, or
   - create a new key pair and download the `.pem` file
5. Under **Network settings / Security group**, allow:
   - **SSH (22)** from **My IP**
   - **HTTP (80)** from `0.0.0.0/0`
6. Launch **2 instances**.
7. Wait until both instances are in the **Running** state and pass status checks.
8. Record their:
   - **Public IPv4 address** or
   - **Public IPv4 DNS**

Example:

- Instance 1: `3.98.10.21`
- Instance 2: `35.182.44.90`

For Ubuntu AMIs, the default SSH username is usually:

```bash
ubuntu
```

---

## Step 2: Store and Secure the `.pem` File

Move your downloaded key to your SSH folder if needed:

```bash
mkdir -p ~/.ssh
mv ~/Downloads/mykey.pem ~/.ssh/
```

Restrict its permissions so SSH will accept it:

```bash
chmod 400 ~/.ssh/mykey.pem
```

Some systems also work with:

```bash
chmod 600 ~/.ssh/mykey.pem
```

If the permissions are too open, SSH will refuse to use the key.

---

## Step 3: Test Direct SSH Access First

Before using Ansible, test SSH manually.

```bash
ssh -i ~/.ssh/mykey.pem ubuntu@3.98.10.21
```

And for the second instance:

```bash
ssh -i ~/.ssh/mykey.pem ubuntu@35.182.44.90
```

If that works, then Ansible will usually work too.

If SSH does not work, check:

- the EC2 instance is running
- the public IP is correct
- the security group allows port 22 from your IP
- the key pair used at launch matches the `.pem` file you have
- the SSH username is `ubuntu`

---

## Step 4: Install Ansible on Your Local Machine

### macOS

```bash
brew install ansible
```

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible
```

### Windows

Use **WSL Ubuntu**, then run the Ubuntu commands above.

Verify installation:

```bash
ansible --version
```

---

## Step 5: Create an Ansible Project Directory

```bash
mkdir -p ~/ansible-aws-ec2
cd ~/ansible-aws-ec2
```

---

## Step 6: Create the Inventory File for AWS EC2 Instances

Create a file named **`inventory.ini`**:

```ini
[web]
3.98.10.21 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem
35.182.44.90 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem
```

You can also use **public DNS names** instead of IPs:

```ini
[web]
ec2-3-98-10-21.ca-central-1.compute.amazonaws.com ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem
ec2-35-182-44-90.ca-central-1.compute.amazonaws.com ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem
```

This tells Ansible:

- which hosts to connect to
- which user to use: `ubuntu`
- which private key file to use: `~/.ssh/mykey.pem`

---

## Step 7: Create `ansible.cfg`

Create **`ansible.cfg`**:

```ini
[defaults]
inventory = ./inventory.ini
host_key_checking = False
retry_files_enabled = False
remote_user = ubuntu
```

This keeps the setup simple for AWS lab work.

---

## Step 8: Verify Connectivity with Ansible

Run:

```bash
ansible all -m ping
```

Expected result:

```bash
3.98.10.21 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
35.182.44.90 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

If you get an error such as **Permission denied (publickey)**, check:

- the `.pem` file path is correct
- the key permissions are correct
- the instance was launched with the same key pair
- the correct username is used

---

## Step 9: Write the Playbook

Create **`site.yml`**:

```yaml
---
- name: Configure AWS Ubuntu EC2 web servers
  hosts: web
  become: true
  gather_facts: true

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Ensure nginx is enabled and running
      service:
        name: nginx
        state: started
        enabled: true

    - name: Deploy a simple homepage
      copy:
        dest: /var/www/html/index.html
        content: |
          <html>
            <head>
              <title>AWS EC2 Ansible Demo</title>
            </head>
            <body style="font-family: Arial; padding: 40px;">
              <h1>Hello from {{ inventory_hostname }}</h1>
              <p>This Ubuntu EC2 instance was configured by Ansible.</p>
              <p>Time: {{ ansible_date_time.iso8601 }}</p>
            </body>
          </html>
        owner: root
        group: root
        mode: '0644'
```

---

## Step 10: Run the Playbook

```bash
ansible-playbook site.yml
```

Ansible should connect to both AWS EC2 instances using the `.pem` file and apply the configuration.

---

## Step 11: Verify in Browser or with `curl`

```bash
curl http://3.98.10.21
curl http://35.182.44.90
```

Or open in your browser:

```text
http://3.98.10.21
http://35.182.44.90
```

You should see the HTML page deployed by Ansible.

---

## Common AWS + `.pem` Troubleshooting

### 1. Permission denied (publickey)

Possible reasons:

- wrong `.pem` file
- wrong path to `.pem`
- wrong SSH username
- instance launched with a different key pair

For Ubuntu, use:

```bash
ansible_user=ubuntu
```

---

### 2. Unprotected private key file

Fix it with:

```bash
chmod 400 ~/.ssh/mykey.pem
```

---

### 3. SSH timeout

Check the security group:

- inbound rule for **port 22**
- source should be **your IP** or a permitted IP range

---

### 4. HTTP page not loading

Check:

- security group allows **port 80**
- Nginx is running
- instance has a public IP

You can verify service status with:

```bash
ansible web -a "systemctl status nginx" -b
```

---

## Optional Improvement: Use Variables for the Key File

Instead of repeating the key path on every line, you can write the inventory like this:

```ini
[web]
3.98.10.21
35.182.44.90

[web:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/mykey.pem
```

This is cleaner and easier to maintain.

---

## Optional Improvement: Use an SSH Config File

You can also simplify access by creating `~/.ssh/config`:

```sshconfig
Host aws-web-1
    HostName 3.98.10.21
    User ubuntu
    IdentityFile ~/.ssh/mykey.pem

Host aws-web-2
    HostName 35.182.44.90
    User ubuntu
    IdentityFile ~/.ssh/mykey.pem
```

Then your inventory becomes:

```ini
[web]
aws-web-1
aws-web-2
```

---

## Summary

To make the original guide suit **AWS EC2 instances and `.pem` files**, the most important AWS-specific points are:

1. Launch EC2 instances with a key pair.
2. Keep the `.pem` file safe and set correct permissions.
3. Use the correct SSH user, usually `ubuntu` for Ubuntu AMIs.
4. Point Ansible inventory to the `.pem` file using:

```ini
ansible_ssh_private_key_file=~/.ssh/mykey.pem
```

5. Make sure AWS security groups allow SSH and HTTP.

