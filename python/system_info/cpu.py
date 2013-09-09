#!/usr/bin/env python
def cpu_stat():
    cpu = []
    cpuinfo = {}
    f = open("/proc/cpuinfo")
    lines = f.readlines()
    f.close()
    for line in lines:
        if line == '\n':
            cpu.append(cpuinfo)
            cpuinfo = {}
        if len(line) < 2: continue
        name = line.split(':')[0].rstrip()
        var = line.split(':')[1]
        cpuinfo[name] = var
    return cpu

print cpu_stat()
