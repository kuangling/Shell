#!/usr/bin/env python
# coding=utf8
# Filename: mem_info1.py
# Last modified: 2013-06-02 10:20
# Author: itnihao
# Mail: itnihao@qq.com
# Description: 

import re
def parse_mem_file(memfile = '/proc/meminfo'):
    with open(memfile, 'r') as meminfo:
        return dict(
            (m.group(1), int(m.group(2)))
            for m in [re.match('(.+):\\s*(\\d+)', line) for line in meminfo]
            if m is not None)

