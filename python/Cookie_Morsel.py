#!/usr/bin/env python
import Cookie
import datetime
def show_cookie(c):
    print c
    for key, morsel in c.iteritems():
        print 
        print 'key =',morsel.key
        print 'value =',morsel.value
        print 'coded_value =',morsel.coded_value
    for name in morsel.keys():
        if morsel[name]:
            print '%s = %s' % (name,morsel[name])

c = Cookie.SimpleCookie()

c['encoded_value_cookie'] = '"cookie_value"'
c['encoded_value_cookie']['comment'] = 'Notice that this cookie value has escaped quotes'

c['restricted_cookie'] = 'cookie_value'
c['restricted_cookie'] ['path'] = '/sub/path'
c['restricted_cookie'] ['secure'] = True

c['with_max_age'] = 'expires in 5 minutes'
c['with_max_age'] ['max-age'] = 300 # seconds

c['expries_at_time'] = 'cookie_value'
expries = datetime.datetime.now() + datetime.timedelta(hours=1)
c['expires_at_time']['expires'] = expires.strftime('%a,%d %b %Y %H:%M:%S')

show_cookie(c)
