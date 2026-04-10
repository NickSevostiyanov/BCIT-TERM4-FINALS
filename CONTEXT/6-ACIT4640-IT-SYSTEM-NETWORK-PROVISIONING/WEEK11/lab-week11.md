Instructions
Setup:

Clone the starter code into your development environment

https://gitlab.com/cit_4640/4640-ansible-roles-lab.git

Create a new `~/.ssh/aws` ssh key

Use the included scripts to add the new key to your aws account

Run the terraform configuration. This will create two servers, one running ubuntu the other running rocky linux.

Tasks:

Start by looking at the included Ansible configuration. This includes a dynamic inventory that uses the aws_ec2 plugin.

Refactor the configuration in "plays.yml" into a new "playbook.yml" file. You can delete the plays.yml file when you have your new configuration working.

Break out configuration into roles for both servers. (two roles)

Any "files" or "templates" should be moved into a role.

Use handlers in the appropriate locations to reload the nginx server when needed.

Add necessary commands to run your Ansible configuration to the README.md file.

Take a victory screenshot of the HTML document that is being served by your ubuntu "frontend" server. Add this screenshot to your README.md file.

Deliverables:

Submit a public git repository that contains the following files

- README.md
- server-img.jpg (this can be a png, or other common image format)
- .gitignore (included, add this before running git commands)
- terraform/
- main.tf
- provider.tf
- modules/
- web-server/
- main.tf
- outputs.tf
- variables.tf
- ansible/
- ansible.cfg
- playbook.yml
- inventory/
- aws_ec2.yml
- roles/
- ... appropriate directory structure for the roles
