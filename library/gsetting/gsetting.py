#!/usr/bin/python

import json
import subprocess

from ansible.module_utils.basic import *


def _split_key(full_key):
    key_array = full_key.split('.')
    schema = '.'.join(key_array[0:-1])
    single_key = key_array[-1]
    return (schema, single_key)


def _set_value(full_key, value):
    schema, single_key = _split_key(full_key)
    command = ['/usr/bin/gsettings', 'set', schema, single_key, str(value)]
    return subprocess.check_output(command).strip()


def _get_value(full_key):
    schema, single_key = _split_key(full_key)
    command = ['/usr/bin/gsettings', 'get', schema, single_key]
    return subprocess.check_output(command).strip()


def main():
    module = AnsibleModule(
        argument_spec = {
            'state': { 'choices': ['present'], 'default': 'present' },
            'key': { 'required': True },
            'value': { 'required': True }
        },
        supports_check_mode = True,
    )

    key = module.params['key']
    value = module.params['value']

    old_value = _get_value(key)
    changed = old_value != str(value)

    if changed and not module.check_mode:
        _set_value(key, value)

    print json.dumps({
        'changed': changed,
        'key': key,
        'value': str(value),
        'old_value': old_value
    })


main()
