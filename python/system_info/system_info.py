#!/usr/bin/env python
# coding=utf8
# Filename: system_info.py
# Last modified: 2013-06-02 09:03
# Author: itnihao
# Mail: itnihao@qq.com
# Description: 

import os, numpy.distutils.cpuinfo

def getSN():
    print "="*20, "Machine hardware information", "="*20
    s= os.popen('dmidecode   -s  system-serial-number')
    n =  os.popen('dmidecode   -s system-product-name')
    sn =  s.readline().strip()
    name =  n.readline().strip()
    s.close()
    if ( len(sn) > 0 ):
        print  "Product Name:", name
        print  "Serial Number:", sn, "\n"
    else:
        return  -1


def mem_info():
    mem_info = open('/proc/meminfo', 'r')
    lines=[mem_dict.replace('kB\n', '').split(":") for mem_dict in mem_info]
    mem_dict=dict((key, int(value)) for (key , value) in lines)
    
    TotalMomery = (mem_dict['MemTotal'])/1024
    UsedMemory  = (mem_dict['MemTotal'] - mem_dict['MemFree'] - mem_dict['Buffers'] - mem_dict['Cached'])/1024
    FreeMemory  = (mem_dict['MemTotal'] - UsedMemory)/1024
    TotalSwap   = (mem_dict['SwapTotal'])/1024
    UsedSwap    = (mem_dict['SwapTotal'] - mem_dict['SwapFree'])/1024
    FreeSwap    = (mem_dict['SwapFree'])/1024 
    print "="*20, "Momery information status", "="*20
    print "TotalMomery is :", TotalMomery, "MB"
    print "UsedMomery  is :", UsedMemory,  "MB"
    print "FreeMemory  is :", FreeMemory,  "MB"
    print "TotalSwap   is :", TotalSwap,   "MB"
    print "UsedSwap    is :", UsedSwap,    "MB"
    print "FreeSwap    is :", FreeSwap,    "MB"

def cpu_info():
    # import multiprocessing
    #print "cpu core number is : ",  + multiprocessing.cpu_count()
    #import platform
    cpuinfo =  numpy.distutils.cpuinfo.cpu.info[0]

    print ""
    print "="*20, "cpu information status", "="*20
    print "cpu core number : ", len(numpy.distutils.cpuinfo.cpu.info)
    print "cpu model name  : ", cpuinfo['model name']
    print "cpu cache size  : ", cpuinfo['cache size']
    print "cpu MHz         : ", cpuinfo['cpu MHz'], "MHz"

def disk_info():
    print ""
    print "="*20, "Harddisk information status", "="*20
    disk_info =  open('/proc/partitions', 'r')
    for disk_name in disk_info:
        print disk_name.replace('\n', '')

def getload():
    read_load=open('/proc/loadavg')
    load_data=read_load.read().split(" ") 
    print ""
    print "="*20,  "load average status","="*20
    print "load average in 1  minutes: ", load_data[0]
    print "load average in 5  minutes: ", load_data[1]
    print "load average in 15 minutes: ", load_data[2]

#def 


getSN()
mem_info()
cpu_info()
disk_info()
getload()
