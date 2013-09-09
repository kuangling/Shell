#!/usr/bin/env python
#wraps up rsync to synchronize two directories

from subprocess import call
import sys
import time

"""this motivated rsync tries to synchronize forever"""

source = "/tmp/sync_dir_A"
target = "/tmp/sync_dir_B"
rsync  = "rsync"
arguments = "-av"
cmd = "%s %s %s %s" % (rsync,arguments,source,target)

def sync():
    while True:
        ret = call(cmd,shell=True)
        if ret !=0:
            print "resubmitting rsync"
            time.sleep(5)
        else:
            print "rsync was successful"
            cmd_mail="echo 'jobs done'|mail -s 'jobs done' itnihao@163.com"
            call(cmd_mail,shell=True)
            sys.exit(0)
sync()
