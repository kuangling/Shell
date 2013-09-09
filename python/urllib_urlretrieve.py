#!/usr/bin/env python

import urllib
import os
def reporthook(blocks_read,block_size,total_size):
    if not blocks_read:
        print 'Connection opened'
        return
    if total_size < 0:
        #Unknow size
        print 'Read %d blocks' % blocks_read
    else:
        amount_read = blocks_read * block_size
        print 'Read %d blocks,or %d %d' % (blocks_read,amount_read,total_size)
        return

try:
    filename, msg = urllib.urlretrieve('http://itnihao.blog.51cto.com/',reporthook=reporthook)
    print
    print 'File:',filename
    print 'Headers:'
    print msg
    print 'File exists before cleanup:',os.path.exists(filename)
finally:
    urllib.urlcleanup()
    print 'File still exists:',os.path.exists(filename)
