#!/usr/bin/env python

from urlparse import urldefrag
orignal = 'http://netloc/path;parameters?query=argument#fragment'
print orignal
url,fragment = urldefrag(orignal)
print url
print fragment
