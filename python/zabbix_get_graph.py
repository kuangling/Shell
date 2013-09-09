__author__ = 'zzr'
import cookielib,urllib2
url_graph = 'http://zabbix.xxx.com/chart2.php?graphid=562&width=616&period=86400&stime=20121202113109'
url='http://zabbix.xxx.com/index.php'

def cookie(url,name,password):
    cookie = cookielib.CookieJar()
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookieProc)
    urllib2.install_opener(opener)

    postdata ='request=&name=%s&password=%s&autologin=1&enter=Sign+in' % (name,password)
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

    req = urllib2.Request(url,data=postdata,headers=header)
    urllib2.urlopen(req).read()

def main():
    cookie(url,'admin','passwd')
    req = urllib2.Request(url_graph)
    png = urllib2.urlopen(req).read()
    file = open('d://test.png','wb')
    file.write(png)
    file.close()

if __name__ == '__main__':
    main()