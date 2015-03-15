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

## Run ansible provisioning
Assuming all went well during the boostrap process, run the following command on your machine:

    ansible-playbook desktop-provisioning.yaml -i inventory --diff --ask-sudo-pass

Which distribution you are running will be auto-detected.
