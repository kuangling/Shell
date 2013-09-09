#!/usr/bin/env python

import subprocess

"""
A ssh based command diapath system
"""
machines = [ "10.10.10.28",
"10.10.10.29",
"10.10.10.30",
"10.10.10.31",
"10.10.10.32"]

cmd = "uname"
for machine in machines:
    subprocess.call("printf '%s OS type is:  ';ssh root@%s %s" % (machine,machine,cmd),shell=True)
