#! /bin/bash 
# author: kuangl
# mial: kuangl@orient-media.com
# date: 2013-05-04
 
awk -F"[" '/disconnect from unknown/ {print $NF}' /var/log/maillog|sed "s/]//g"|sort -nr|uniq -c|sort|awk '{print $1"="$2}' >/root/bad_ip_tmp.txt
awk -F":" '/verification failed/ {print $5}' /var/log/maillog|grep -v "SASL"|sort -nr|uniq -c|awk '{print $1"="$2}' >>/root/bad_ip_tmp.txt
awk -F"-" '/\/phpmyadmin\/scripts\/setup\.php/  {print $1}' /var/log/httpd/access_log |grep -v "180.166.44.226" |sort -nr|uniq -c |sort  -n |awk '{print $1"="$2}' >>/root/bad_ip_tmp.txt
awk -F"-" '/ZmEu/ {print $1}' /var/log/httpd/access_log |grep -v "180.166.44.226" |sort -nr|uniq -c |sort  -n |awk '{print $1"="$2}' >>/root/bad_ip_tmp.txt
sort /root/bad_ip_tmp.txt|uniq >/root/bad_ip.txt
DEFINE="2"  
for i in $(cat  /root/bad_ip.txt)
do  
   NUM=`echo $i |awk -F"=" '{print $1}'`  
   IP=`echo $i|awk  -F"=" '{print $2}'`  
   if [ $NUM -ge $DEFINE ];  
      then  
         iptables -L -n|grep $IP > /dev/null
         if [ $? -gt 0 ];  
            then  
               iptables -I RH-Firewall-1-INPUT 4 -s $IP -j DROP
         fi  
   fi  
done
