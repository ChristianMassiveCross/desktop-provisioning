#!/usr/bin/python

import json
import re
import subprocess

from ansible.module_utils.basic import *


def _escape_single_quotes(string):
    return re.sub("'", r"'\''", string)


def _set_value(key, value):
    command = ['/usr/bin/dconf', 'write', key,
            "'%s'" % _escape_single_quotes(value)]
    return subprocess.check_output(command).strip()


def _get_value(key):
    command = ['/usr/bin/dconf', 'read', key]
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
        'old_value': old_value,
    })


main()
