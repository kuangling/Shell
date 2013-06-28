#!/bin/bash
# author: kuangl
# mail:kuangl@orient-media.com
# 

# -------------------------------------------------------- #
                   ## Ipvsadm_install
# -------------------------------------------------------- #

# ipvsadm installation
CURRENT_PATH=$(pwd)


for i in $(rpm -q gcc gcc-c++ kernel-devel openssl-devel popt-devel popt-static libnl-devel |grep 'not installed' | awk '{print $2}')
do 
    yum -y install $i
done 
	

[ -d ${CURRENT_PATH}/software ]
[ "$?" != 0 ] && mkdir ${CURRENT_PATH}/software
cd ${CURRENT_PATH}/software
[ ! -e ipvsadm-1.26.tar.gz ] && wget http://www.linuxvirtualserver.org/software/kernel-2.6/ipvsadm-1.26.tar.gz
tar -zxvf ipvsadm-1.26.tar.gz
cd ipvsadm-1.26
make && make install
echo $? || [ $? != 0  ] || echo  " installation  ipvsadm  failed" || exit 1

echo "modprobe ip_vs" >> /etc/rc.local

# ipvsadm start-up 
[ -x ${CURRENT_PATH}/scripts/ipvsadm  ] && [ "$?" != 0 ] && chmod 755 ${CURRENT_PATH}/scripts/ipvsadm
cp ${CURRENT_PATH}/scripts/ipvsadm  /etc/init.d/
chkconfig --add ipvsadm
chkconfig --level 345 ipvsadm on
service ipvsadm start


# -------------------------------------------------------- #
                 ## Keepalived_intsall
# -------------------------------------------------------- #

# Keepalived installation


cd ${CURRENT_PATH}/software
[ ! -e keepalived-1.2.4.tar.gz ] &&  wget http://www.keepalived.org/software/keepalived-1.2.4.tar.gz
tar -zxvf keepalived-1.2.4.tar.gz 
cd keepalived-1.2.4
ln -s /usr/src/kernels/$(uname -r) /usr/src/kernels/linux
./configure --prefix=/usr  --bindir=/usr/bin  --sbindir=/usr/bin  --libexecdir=/usr/libexec --localstatedir=/var --libdir=/lib64  --infodir=/usr/share/info  --sysconfdir=/etc --mandir=/usr/local/share/man   --with-kernel-dir=/usr/src/kernels/linux
make && make install
echo $? || [ $? != 0  ] || print " installation keepalived  failed" || exit 1
chkconfig --add keepalived
chkconfig --level 345 keepalived on
