#!/usr/bin/env python

import os

from urllib import pathname2url,url2pathname

print '== Default =='
path = '/a/b/c'
print 'Original:',path
print 'URL     :',pathname2url(path)
print 'path    :',url2pathname('/d/e/f')
print 

from neturl2path import pathname2url,url2pathname

print '== Windows,without drive letter =='
path = path.replace('/','\\')
print 'Original:',path
print 'URL     :',pathname2url(path)
print 'path    :',url2pathname('/d/e/f')
print 

print '== Windows,without drive letter =='
path = 'C:\\'+ path.replace('/','\\')
print 'Original:',path
print 'URL     :',pathname2url(path)
print 'path    :',url2pathname('/d/e/f')
print

