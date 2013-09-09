#!/usr/bin/env python

import os, sys
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]


for dir_name,sub_dirs,files in os.walk(root):
    print '\n',dir_name
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    contents = sub_dirs + files
    contents.sort()
    for c in contents:
        print '\t%s' % c
