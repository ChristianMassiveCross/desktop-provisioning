#!/bin/sh
echo "Make sure you have put in ssh keys before running this"
sudo apt-get update
sudo apt-get install git python-pip python-yaml python-jinja2
sudo pip install ansible==1.8.2
git config --global user.name "Oolong Brothers"
git config --global user.email oolongbrothers@gmx.net
cd ~
mkdir Code
cd Code
git clone git@github.com:oolongbrothers/desktop-provisioning.git
cd desktop-provisioning
