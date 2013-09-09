#!/usr/bin/env python

import os

print 'String:',os.getcwd()
print os.listdir(os.curdir)

print 'Moving up one:',os.pardir
os.chdir(os.pardir)

print 'After move:',os.getcwd()
print os.listdir(os.curdir)


