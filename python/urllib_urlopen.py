#!/usr/bin/env python

import urllib

response = urllib.urlopen('http://localhost/')
print 'RESPONSE:',response
print 'URL     :',response.geturl()

headers = response.info()
print 'DATE    :',headers['date']
print 'HEADERS :'
print '---------'
print headers

data = response.read()
print 'LENGTH  :',len(data)
print 'DATA    :'
print '---------'
print data
