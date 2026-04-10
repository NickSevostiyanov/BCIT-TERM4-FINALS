Guide: Ansible on Ubuntu EC2 (Install & Configure Two Instances)

This quick, reliable walkthrough installs **Ansible** on your laptop and uses it to configure **two Ubuntu EC2 instances** (install Nginx and deploy a simple homepage).

---

## Prerequisites

- An AWS account with permissions to launch EC2.
- A downloaded EC2 key pair file (e.g., `~/.ssh/mykey.pem`).

---

## Launch 2 Ubuntu EC2 Instances

1. **AWS Console → EC2 → Launch instances**
   - **AMI:** *Ubuntu Server 22.04 LTS (amd64)*
   - **Instance type:** `t2.micro`
   - **Key pair:** create/download `mykey.pem`
   - **Security group rules:**
     - **SSH (22):** from your IP
     - **HTTP (80):** from anywhere (0.0.0.0/0)
2. Wait for both instances to pass status checks.
3. Note each instance’s **Public IPv4 address** as `IP1` and `IP2`.
4. Default SSH user for Ubuntu AMIs: **`ubuntu`**

---

## Install Ansible on Your Laptop

### macOS (Homebrew)
```bash
brew install ansible
```

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible
```

### Windows
Use **WSL (Ubuntu)** and run the Ubuntu commands above.

**Secure your key file:**
```bash
chmod 600 ~/.ssh/mykey.pem
```

---

## Create a Minimal Ansible Project

```bash
mkdir -p ~/ansible-ubuntu-ec2 && cd ~/ansible-ubuntu-ec2
```

Create **`inventory`** (replace with your public IPs and key path):
```ini
[web]
IP1 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem
IP2 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/mykey.pem
```

Create **`ansible.cfg`**:
```ini
[defaults]
inventory = ./inventory
host_key_checking = False
retry_files_enabled = False
```

---

## Verify SSH Connectivity with Ansible

```bash
ansible all -m ping
```

**Expect:** each host returns `pong`.

If there’s an error:
- Confirm security group allows **SSH (22)** from your IP.
- Ensure `ansible_user=ubuntu` in `inventory`.
- Check key permissions: `chmod 600 ~/.ssh/mykey.pem`.

---

## Write the Playbook (Install Nginx + Homepage)

Create **`site.yml`**:
```yaml
---
- name: Configure Ubuntu web servers
  hosts: web
  become: true
  gather_facts: true

  tasks:
    - name: Update apt cache (valid for 1 hour)
      apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Enable and start nginx
      service:
        name: nginx
        state: started
        enabled: true

    - name: Deploy simple index page
      copy:
        dest: /var/www/html/index.html
        content: |
          <html>
            <head><title>Ansible Ubuntu Demo</title></head>
            <body style="font-family:Arial;">
              <h1>Hello from {{ inventory_hostname }}</h1>
              <p>Provisioned by Ansible at {{ ansible_date_time.iso8601 }}</p>
            </body>
          </html>
        owner: root
        group: root
        mode: '0644'
```

---

## Run the Playbook

```bash
ansible-playbook site.yml
```

**Expect:** `changed`/`ok` results for both hosts without errors.

---

## Verify

```bash
curl http://IP1
curl http://IP2
```

Or open `http://IP1` and `http://IP2` in a browser. You should see the demo page showing each host’s name.

---

## Quick Troubleshooting

- **SSH timeout / permission denied:**
  - Security group must allow **port 22** from your IP.
  - Use `ansible_user=ubuntu`.
  - `chmod 600 ~/.ssh/mykey.pem`.

- **HTTP not reachable:**
  - Security group must allow **port 80** from `0.0.0.0/0`.

- **UFW (if you enabled it manually):**
  ```bash
  sudo ufw allow 'Nginx HTTP'
  sudo ufw status
  ```

---

## Re-Run Safely (Idempotency)

Re-running:
```bash
ansible-playbook site.yml
```
will make no changes unless something drifted, thanks to Ansible’s idempotent tasks.

---

## Optional Next Steps

- Replace static IPs with **AWS EC2 Dynamic Inventory** using tags.
- Add **TLS** (Let’s Encrypt / certbot) and a domain in Route 53.
- Refactor into **roles** for cleaner structure.
