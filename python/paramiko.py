#!/usr/bin/env python

import paramiko

hostname = '127.0.0.1'
port = 60022
username = 'root'
password = ''

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname,port,username,passwqord)
    stdin,stdout,stderr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()
