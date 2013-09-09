#!/usr/bin/env python

import os

TEST_GID=500001
TEST_UID=500001

def show_user_info():
    print 'Effective User   :',os.geteuid()
    print 'Effective Group  :',os.getegid()
    print 'Actual    User   :',os.getuid(),os.getlogin()
    print 'Actual    Group  :',os.getgid()
    print 'Actual    Groups :',os.getgroups()
    return

print 'BEFORE CHANGE:'
show_user_info()
print   


try:
    os.setegid(TEST_GID)
except OSError:
    print 'ERROR: Could not change effective group. Re-run as root.'
else:
    print 'CHANGE_GROUP:'
    show_user_info()
    print


try:
    os.seteuid(TEST_UID)
except OSError:
    print 'ERROR: Could not change effective user. Re-run as root.'
else:
    print 'CHANGE_USER:'
    show_user_info()
    print
   
