#!/bin/sh
echo "Make sure you have put in ssh keys before running this"
echo disable > /sys/firmware/acpi/interrupts/gpe66
sudo yum update
sudo yum install python-pip python-yaml python-jinja2 python-crypto

#common part
sudo pip install ansible==1.9.0.1
git config --global user.name "Oolong Brothers"
git config --global user.email oolongbrothers@gmx.net
git config --global push.default simple
cd ~
mkdir Code
cd Code
git clone git@github.com:oolongbrothers/desktop-provisioning.git
cd desktop-provisioning

