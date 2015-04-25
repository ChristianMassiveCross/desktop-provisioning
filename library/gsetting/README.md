ansible-gsetting
================

Ansible module for setting GSettings entries.

This module is based on based on [https://github.com/jistr/ansible-gsetting]

See also
[ansible-dconf](https://github.com/jistr/ansible-dconf).

Installation
------------

    Copy the files in this folder into an ansible library folder ~/ansible_dir/library/gsetting

Usage examples
--------------

    - name: Do not remember mount password
      gsetting: key=org.gnome.shell.remember-mount-password value=false

    - name: Shortcut panel-main-menu
      gsetting: key=org.gnome.desktop.wm.keybindings.panel-main-menu value="@as []"

Be careful with string values, which should be passed into GSetting
single-quoted. You'll need to quote the value twice in YAML:

    - name: Use list view by default in nautilus
      gsetting: key=org.gnome.nautilus.preferences.default-folder-viewer value="'list-view'"

    - name: Define list view columns in nautilus
      gsetting: key=org.gnome.nautilus.list-view.default-visible-columns value="['name', 'size', 'date_modified', 'permissions', 'owner', 'group']"
