# -*- coding:utf-8 -*- #


import socket
import wmi

def hostname():
    """
    主机名
    """
    return socket.gethostname()

def iplist():
    """
    ip地址列表
    格式:('OUZSIZZDE4HUA3B', [], ['192.168.1.4', '192.168.137.1', '192.168.168.1'])
    """
    iplist = socket.gethostbyname_ex(hostname())
    return ",".join(iplist[2])


def oid():
    """
    oid信息，最多3快网卡的mac
    """
    #mac = getMACs()
    #a = []
    #for i in mac:
        #a.append(str(i).replace('-',''))
    c = wmi.WMI ()
    mac = []
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
        #interface_des = interface.Description
        #if interface_des.split()[0] != 'VMware':
        mac.append((interface.MACAddress).replace(':',''))
        #for ip_address in interface.IPAddress:
            #if ip_address.find(':') < 0:
                #print ip_address
    #倒叙
    mac.reverse()
    if len(mac) > 3:
        oid = "".join(mac[0:3]).lower()
    else:
        oid = "".join(mac).lower()
        
    return oid

def cpuinfo():
    """
    cpu信息
    """
    c = wmi.WMI ()
    for cpu in c.Win32_Processor():
        return cpu.Name

def meminfo():
    """
    内存信息
    """
    c = wmi.WMI () 
    cs = c.Win32_ComputerSystem() 
   
    mem = int(cs[0].TotalPhysicalMemory)/1024/1024 
    return str(mem) + 'MB'

def ipinfo():
    """
    接口名称和ip地址
    """
    c = wmi.WMI ()
    osIP = ""
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
        #interface_des = interface.Description
        #if interface_des.split()[0] != 'VMware':
        osIP = osIP + interface.Description + ":"
        for ip_address in interface.IPAddress:
            if ip_address.find(':') < 0:
                osIP = osIP + ip_address + ","

    return osIP.strip()[:-1]


def macineType():
    """
    服务器型号
    """
    c = wmi.WMI ()
    for board_id in c.Win32_BaseBoard():
        return board_id.Product
    
    
def serialnumber():
    """
    序列号
    """
    c = wmi.WMI ()
    for board_id in c.Win32_BaseBoard():
        return board_id.SerialNumber
    
    
def diskinfo():
    """
    硬盘信息
    """

    c = wmi.WMI ()
    d = []
    for i in c.Win32_DiskDrive():
    
        try:
            i = "%s:%dG" % (i.Caption, long(i.Size)/1000/1000/1000)
            d.append(i)
        except:
            pass
        
    return ",".join(d)