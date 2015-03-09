#!/bin/sh
echo "Make sure you have put in ssh keys before running this"
echo disable > /sys/firmware/acpi/interrupts/gpe66
sudo apt-get update
sudo apt-get install git python-pip python-yaml python-jinja2

source ./bootstrap-all.sh
