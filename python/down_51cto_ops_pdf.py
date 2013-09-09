#!/usr/bin/env python
# coding=utf8
# Filename: down_51cto_ops_pdf.py
# Last modified: 2013-04-18 11:22
# Author: itnihao
# Mail: itnihao@qq.com

'''
=========即将下载51cto《Linux运维趋势》所有pdf=========
当前目录下创建51cto_ops_pdf文件夹，下载后的文件保存于此
'''
import os,urllib2, re
#pdf下载地址
URL =  "http://os.51cto.com/down/?dir=linuxops"

#判断51cto_ops_pdf文件是否存在
if not os.path.isdir('51cto_ops_pdf'):
    print "51cto_ops_pdf dirctory is missed, it will be created"
    os.mkdir('51cto_ops_pdf')
    os.chdir('51cto_ops_pdf')
else:
    os.chdir('51cto_ops_pdf')

s=  urllib2.urlopen(URL).read()
pat =  re.compile(r'http://.+?.pdf"')
urls=  re.findall(pat,s)
print __doc__
for i in urls:
     url =  i.replace('"',  '')
     #页面抓取的url为http://os.51cto.com/downlinuxops/51cto_linuxops_issue23.pdf
     #实际下载地址h为http://os.51cto.com/down/linuxops/51cto_linuxops_issue23.pdf
     url =  url.replace('downlinuxops', 'down/linuxops')
     #获取文件名
     pdf_name =  os.path.basename(url)
     #下载保存文件
     if not os.path.isfile(pdf_name):
         try:
             conn= urllib2.urlopen(url)
             data = conn.read()
             print "downloading"  +  url + "*"*24
             with open(pdf_name,'wb') as pdf:
                 pdf.write(data)
         except:
             print url,"url error"

