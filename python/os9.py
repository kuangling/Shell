#!/usr/bin/env python

import os
import tempfile

link_name = tempfile.mktemp( )
print link_name

print "Creating link"
os.symlink(__file__,link_name)
print __file__

stat_info = os.lstat(link_name)
print 'Permissions:',oct(stat_info.st_mode)

print 'Points to:',os.readlink(link_name)

os.unlink(link_name)
