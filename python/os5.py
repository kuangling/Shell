#!/usr/bin/env python

import os

print 'Testing:',__file__
print 'Exists:',os.access(__file__,os.F_OK)
print 'Readable:',os.access(__file__,os.R_OK)
print 'Writeable:',os.access(__file__,os.W_OK)
print 'Executable:',os.access(__file__,os.X_OK)
