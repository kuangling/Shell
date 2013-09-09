#!/usr/bin/env python

import os


print '\npopen, read:'
pipe_stdout = os.popen('echo "to stdout"','r')
try:
    stdout_value = pipe_stdout.read()
finally:
    pipe_stdout.close()
print '\nstdout:', repr(stdout_value)

print '\npopen,write:'
pipe_stdin = os.popen('cat -','w')
try:
    pipe_stdin.write('\tstdin: to stdin\n')
finally:
    pipe_stdin.close()


popen, read
    stdout:  'to stdout\n'

popen, write:
    stdin: to stdin

