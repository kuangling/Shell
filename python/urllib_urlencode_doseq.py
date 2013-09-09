#!/usr/bin/env python

import urllib
query_args = { 'foo':['fool','fool2']}
print 'Single :',urllib.urlencode(query_args)
print 'Sequence:',urllib.urlencode(query_args,doseq=True)
