#!/bin/bash
source /etc/bashrc
source /etc/profile

	MYSQL_PASSWORD=harry
	BACKUP_SERVER=192.168.1.89
	[ -d /mysql_backup ] 
	[ "$?" != 0 ] && mkdir /mysql_backup
	cd /mysql_backup
for DABASE_NAME in $(mysql -uroot -p${MYSQL_PASSWORD} -e 'show databases'|grep -v Database|grep -v information)
do
	mysqldump -uroot -p${MYSQL_PASSWORD}   ${DABASE_NAME} >$(date '+%Y%m%d')${DABASE_NAME}.sql
	rm $(date +%Y%m%d --date='5 days ago')${DABASE_NAME}.sql
	sleep 15
done
