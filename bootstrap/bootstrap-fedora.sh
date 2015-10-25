#!/bin/sh
echo "Make sure you have put in ssh keys before running this"
read -p "Press [Enter] key to start boostrap process..."
sudo su -c "echo 'deltarpm=0' >> /etc/dnf/dnf.conf"
sudo dnf update -y
sudo dnf install -y python-pip python-yaml python-jinja2 python-crypto

#common part
sudo pip install ansible==1.9.4
git config --global user.name "Oolong Brothers"
git config --global user.email oolongbrothers@gmx.net
git config --global push.default simple
cd ~
mkdir Code
cd Code
git clone git@github.com:oolongbrothers/desktop-provisioning.git
cd desktop-provisioning
echo "If you have any, put your custom localhost.yaml host_vars file into ~/Code/desktop-provisoning/inventories/host_vars/localhost.yaml"
echo "Then run: cd ~/Code/desktop-provisoning; ansible-playbook desktop-provisioning.yaml -i inventories/inventory --diff --ask-sudo-pass"
