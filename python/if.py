#!/usr/bin/env python
def fib(n):
    print 'n=',n
    if 5 > n > 1:
        return fib(n+1) 
    else:
        print 'end of the line'
        return 1
fib(2)
