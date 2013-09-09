#!/usr/bin/env python

import os
import sys
import time

for i in range(3):
    print 'PARENT: Forking %s' % i
    worked_pid = os.fork()
    if not worked_pid:
        print 'WORKED %s: Starting' % i
        time.sleep(2 + i)
        print 'WORKED %s: Finishing' % i
        sys.exit(i)

for i in range(3):
    print 'PARENT: Waiting for %s' % i
    done=os.wait()
    print 'PARENT:', done
