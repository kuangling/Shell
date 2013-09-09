#!/usr/bin/env python


try:
    import cPickle as pickle
except:
    import pikcle
import pprint
from StringIO import StringIO

class SimpleObject(object):

    def __init__(self,name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.joint(1)
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject9('last'))

#Simalate a file with StringIO
out_s = StringIO()

#Write to the stream
for o in data:
    print 'WARNING: %s (%s)' % (o.name,o.name_backwards)
    pickle.dump(o,out_s)
    out_s.flush()

#Set up a read-able stream
in_s = StringIO(out_s.getvalue())

#Read the data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print 'READ: %s (%s)' % (o.name,o.name_backwards)

