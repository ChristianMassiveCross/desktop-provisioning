# desktop-provisioning
Ansible provisioning for my desktop machines running Linux

## Supported environments
Hardware:
* MacBook Pro 11,1

Distributions:
* Fedora 21
* Ubuntu 14.10

## Bootstrapping your machine
Run the script corresponding to your distribution from the `bootstrap` folder.

* Fedora 21 - `boostrap-fedora.sh`
* Ubuntu 14.10 - `boostrap-ubuntu.sh`

## Configuration

You need to configure your desktop provisioning setup. To do so, copy the `inventories/host_vars/localhost.yaml.example` filr to `inventories/host_vars/localhost.yaml` and replacing the example values with ones that actually match your environment. That file is excluded from source control. 

## Run ansible provisioning
Assuming all went well during the boostrap process, run the following command on your machine:

    ansible-playbook desktop-provisioning.yaml -i inventories/inventory --diff --ask-sudo-pass

Which distribution you are running will be auto-detected.
