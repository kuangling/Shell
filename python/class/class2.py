#!/usr/bin/env python

class Foo(object):
    @staticmethod
    def add(x,y):
        return x + y
x=Foo.add(4,5)
print x
