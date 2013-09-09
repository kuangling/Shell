#!/usr/bin/env python
# coding=utf8
# Filename: manager_server.py
# Last modified: 2013-04-22 12:31
# Author: itnihao
# Mail: itnihao@qq.com
# Description:

from fabric.api import  run, env

env.user =  'root'
#env.password =  'root'
env.port =  60022
env.hosts=  ['10.10.10.116', '10.10.10.117']
#env.passwords   =     {'root@172.16.102.202':'123',  'root@172.16.102.200':'123'}

def list_uname():
    run('uname  -a')
def list_host():
    run("ip a'")

