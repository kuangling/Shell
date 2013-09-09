#!/usr/bin/env python

from urlparse import urlsplit
parsed = urlsplit('http://user:pass@NetLoc:80/path;parameters/path2;parameters2?query=argument#fragment')
print  parsed
print 'scheme   :',parsed.scheme
print 'netloc   :',parsed.netloc
print 'path     :',parsed.path
print 'query    :',parsed.query
print 'fragment :',parsed.fragment
print 'username :',parsed.username
print 'password :',parsed.password
print 'hostname :',parsed.hostname,'(netloc in lower case)'
print 'port     :',parsed.port
