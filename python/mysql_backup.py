#!/usr/bin/env python

import os,subprocess,datetime

USERNAME = 'root'
PASSWORD = 'harry'
HOSTNAME = 'localhost'
DEL_DAYS = 5
CUR_TIME = datetime.date.today()
AGO_TIME = datetime.timedelta(days=DEL_DAYS)
DEL_TIME = CUR_TIME - AGO_TIME
DATABASE = ''
def mysqldump():
    if os.path.isdir('/mysql_backup'):
        os.chdir('/mysql_backup')
    else:
        os.mkdir('/mysql_backup')
        os.chdir('/mysql_backup')
    database_cmd=[subprocess.call("mysql -u%s -p%s -h%s -e 'show databases'|grep -v Database|grep -v information" %(USERNAME,PASSWORD,
HOSTNAME),shell=True)
    for DATABASE  in database_cmd:
        MYSQLDUMP_FILENAME="/mysql_backup/%s%s.sql"%(CUR_TIME,DATABASE)
        subprocess.call("mysqldump -u%s -p%s -h%s %s>%s" %(USERNAME,PASSWORD,HOSTNAME,DATABASE,MYSQLDUMP_FILENAME),shell=True)
        subprocess.call("rm ${DEL_TIME}${DATABASE}.sql",shell=True)
mysqldump()
