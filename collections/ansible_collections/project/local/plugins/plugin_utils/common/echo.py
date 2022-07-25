#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The echo filter plugin
"""
from __future__ import absolute_import, division, print_function

from ansible.errors import AnsibleFilterError

__metaclass__ = type

def _raise_error(msg):
    """Raise an error message, prepend with filter name
    :param msg: The message
    :type msg: str
    :raises: AnsibleError
    """
    error = "Error when using plugin 'echo': {msg}".format(msg=msg)
    raise AnsibleFilterError(error)


def echo(**kwargs):
    """echo implementation
    """
    # Enter plugin logic here
    # This method will be invoked from the main plugin class
    return kwargs