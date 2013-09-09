#!/usr/bin/env python

from recurse import recurse

def main():
    print 'This is the main program.'
    recurse(2)
    return

if __name__== '__main__':
    main()

def recurse(level):
    print 'recurse(%s)' % level
    if level:
        recurse(level-1)
    return

def not_called():
    print 'This function is never called.'      
