AWX is a modern web UI (User Interface) and API (Application Programming interface) to manage your organization's Ansible Playbook, Inventories, Vault, and Credentials. It is the Open-Source upstream project of the Ansible Automation Controller (formerly Ansible Tower).

FEATURES OF AWX:

Playbook- Playbook is used to executed tasks in the correct order and with    appropriate   parameters, playbook file save in. yaml extension		

Invetory- inventory file contained host address

API- Apis are used in awx

Workflow- The only job of a workflow is to trigger other jobs in specific orders to achieve certain goals.

Templates- Templates can be used to store common variables, snippets of code, or even entire playbook.

Teams- Teams provide a powerful and flexible approach to organizing, controlling, and managing access in Ansible AWX.


![image](https://github.com/abhi798949/awx/assets/120705695/437ee234-ea50-4470-9da2-2f7ca9329918)

INSTALLATION PROCESS:

Before installing the  awx-ansible ,We need install some prerequired tool.

Ubuntu 20.04 or Later

Python3

Ansbile

Docker

Commands for Installation:
$ sudo apt install python-setuptools -y

$ sudo apt install python3-pip -y

$ sudo pip3 install ansible

$ ansible --version

$ sudo apt install docker docker.io -y

$ docker version

$ sudo pip3 install docker-compose

$ docker-compose version

$ sudo usermod -aG docker $USER

$ sudo apt install git vim pwgen -y

$systemctl start docker

$ systemctl enable docker

$ systemctl status docker

$ sudo apt install docker-compose -y

$ docker-compose version

$ sudo apt install nodejs npm -y

$ sudo npm install npm –global

Till now we are completed installation process of prerequired tools.

Now interface github and awx .
github link :

$ wget https://github.com/ansible/awx/archive/17.1.0.zip

$ unzip 17.1.0.zip

Now install AWX:

$ cd awx-17.1.0/installer

/awx-17.1.0/installer:$ pwgen -N 1 -s 30
A key will generated here copy that key it will be used in inventory

/awx-17.1.0/installer:$ nano inventory

Their will be default credentials in the inventory, shoul modify the details and paste the secret key which is generated in previous step
admin_username:
enable admin_password:
secret key: 

/awx-17.1.0/installer:$ ansible-playbook -i inventory install.yml

This command will run the inventory and execute all the dependencies in the inventory if you faced any errors you have done mistake in previous steps then you nedd check previous steps once again

/awx-17.1.0/installer:$ dockers ps -a

It will show the container ID, Images,ports,names...if you not not get any of these your installation has failed..check it and try again

Go to your local browser type https://ubuntuipaddress or http://localhost


![image](https://github.com/abhi798949/awx/assets/120705695/233a6dff-0f07-4dea-ab41-b1f94ad216ac)


The below Image show the work flow of the AWX


![image](https://github.com/abhi798949/awx/assets/120705695/1afd4e8b-f88a-4c14-b517-e8b40f207b4c)













