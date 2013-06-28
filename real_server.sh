#!/bin/bash
# author: kuangl
# mail: kuangl@orient-meida.com
# description: The configuration file to configure the real server.

# -------------------------------------------------------- #
                # REAL_SEVER_CONFINGE_FILE
# -------------------------------------------------------- #

# source function library
. /etc/rc.d/init.d/functions

# Real server IP configure 
LVS_VIP=192.168.122.15
NET_MAST=255.255.255.255

start()
{
      # Start daemons.
      ifconfig lo:0 $LVS_IP netmask $NET_MASK broadcast $LVS_IP
      route add -host $LVS_IP dev lo:0
      echo "1" > /proc/sys/net/ipv4/conf/lo/arp_ignore
      echo "1" > /proc/sys/net/ipv4/conf/all/arp_ignore
      echo "2" > /proc/sys/net/ipv4/conf/lo/arp_announce
      echo "2" > /proc/sys/net/ipv4/conf/all/arp_announce
      echo "RealServer Start OK"
}

stop()
{
      ifconfig lo:0 down
      route del $LVS_IP 
      echo "RealServer Stop  OK"

}


case "$1" in
  start)
       start
  ;;

  stop)
      stop
  ;;

  *)
    echo $"Usage: $0 {start|stop}"
    exit 1
esac
exit $?
                 

