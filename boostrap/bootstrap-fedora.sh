#!/bin/sh
echo "Make sure you have put in ssh keys before running this"
echo disable > /sys/firmware/acpi/interrupts/gpe66
sudo yum update
sudo yum install python-pip python-yaml python-jinja2 python-crypto

source includes/common.sh
