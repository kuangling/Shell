#!/usr/bin/env python

import pprint
import pickle

data1 = [ {'a':'A','b':2,'c':3.0} ]
print 'BEFORE:',
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print 'AFTER:',
pprint.pprint(data2)

print id(data1)
print id(data2)
print 'SAME?:', (data1 is data2)
print 'EQUAL?:', (data1 == data2)

