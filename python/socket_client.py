#!/usr/bin/env python

import socket

s=socket.socket()
s.connect(('192.168.1.89',80))
print s.send("GET / HTTP/1.0\n\n")
print s.recv(200)
s.close()

print socket.getfqdn()

