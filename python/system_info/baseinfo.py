# -*- coding:utf-8 -*- #


import dmidecode
import socket
from common.components import mypopen
import re

def meminfo():
    """
    内存信息
    返回格式:128MB * 1
    """
    mem = dmidecode.memory()
    memDict = {}
    for k,v in mem.iteritems():
        try:
            size = v['data']['Size']
            if size != None:
                if len(memDict) == 0:
                    memDict[size] = 1
                else:
                    if memDict.has_key(size):
                        count = memDict[size] 
                        memDict[size] = sum([count,1])
                    else:
                        memDict[size] = 1
        except:
            pass
    
    m = ""
    for k,v in memDict.iteritems(): 
        m = m + str(k).replace(" ","") + "*" + str(v) + " "
            
    return m.strip().replace(" ",",")


def macineType():
    """
    服务器型号
    """
    sysinfo = dmidecode.system()
    
    for k,v in sysinfo.iteritems():
        try:
            machine_type = v['data']['Product Name']
            if machine_type != "":
                return machine_type
        except:
            pass
        
def serialnumber():
    """
    序列号
    """
    sm = dmidecode.system()

    for k,v in sm.iteritems():
        try:
            sn = v['data']['Serial Number']
            if sn != "":
                return sn
        except:
            pass
        
def hostname():
    """
    主机名
    """
    return socket.gethostname()

def diskinfo():
    """
    硬盘信息
    """
    cmd = 'fdisk -l |grep -v mapper'
    
    stdoutdata,stderrdata = mypopen(cmd).communicate()
    
    key = re.compile('Disk /dev/(.*),')
    
    a = re.findall(key,stdoutdata)
    
    return ",".join(a)


def ipinfo():
    """
    接口名称和ip地址
    """
    from common import components
    
    if components.python_ver() <= '2.5':
        if components.arch() == 'x86_64':
            from lib64.p24 import netifaces
        else:
            from lib.p24 import netifaces
    else:
        if components.arch() == 'x86_64':
            from lib64.p26 import netifaces
        else:
            from lib.p26 import netifaces
    
    osIp = ""
    for i in netifaces.interfaces():
        if i != 'lo' and i != 'usb0' and i != 'sit0':
            try:
                dictIface = netifaces.ifaddresses(i)[2]
                if len(dictIface) > 1:
                    for all_ip in dictIface:
                        strIP = strIP + all_ip['addr'] + " "
                    osIp = osIp + i + ":" +strIP + " "
                else:
                    #得到网卡类型和ip
                    osIp = osIp + i + ":" +dictIface[0]['addr'] + " "
                    #得到ip地址
                    #osIp = osIp + dictIface[0]['addr'] + " "
            except KeyError:
                pass
            
    return osIp.strip().replace(' ',',')