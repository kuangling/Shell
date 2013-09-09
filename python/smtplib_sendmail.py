#!/usr/bin/env python

import smtplib
import email.utils
from email.mime.text import MIMEText

msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient','itnihao@qq.com'))
msg['From'] = email.utils.formataddr(('Author','972322817@qq.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP()
server.set_debuglevel(True)
try:
    server.sendmail('itnihao@qq.com',['972322817@qq.com'],msg.as_string())
finally:
    server.quit()
