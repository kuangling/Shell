#/usr/bin/env python

import os.path

for path in ['/tmp', '/etc', '/', ',']:
    print '"%s" : "%s"' % (path,os.path.split(path))
