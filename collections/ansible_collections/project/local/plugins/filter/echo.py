#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The echo filter plugin
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
name: echo
author: Bradley Thornton (@cidrblock)
version_added: "1.0.0"
short_description: Return the provided value unmodified
description:
    - Return the provided value unmodified
 
options:
  var:
    description:
    - The value to be returned
    type: raw
    required: True
"""

EXAMPLES = """
"""

from ansible.errors import AnsibleFilterError
from ansible_collections.project.local.plugins.plugin_utils.common.echo import (
    echo,
)
from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
    AnsibleArgSpecValidator,
)

def _echo(*args, **kwargs):
    keys = ['var']
    data = dict(zip(keys, args))
    data.update(kwargs)
    aav = AnsibleArgSpecValidator(
        data=data, schema=DOCUMENTATION, name="echo"
    )
    valid, errors, updated_data = aav.validate()
    if not valid:
        raise AnsibleFilterError(errors)
    return echo(**updated_data)

class FilterModule(object):
    """ echo filter plugin"""

    def filters(self):
        """a mapping of filter names to functions"""
        return {"echo": _echo}
