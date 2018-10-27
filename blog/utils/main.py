#!/usr/bin/python
import smtplib
from email.message import EmailMessage
from blog.utils import MailUtils

prepMessage = MailUtils.getBodyMesage("2018-12-11")

gmail_user = 'r.holdberh@gmail.com'
gmail_password = ''

sent_from = gmail_user
to = ''
subject = 'BLAA'

msg = EmailMessage()
msg['Subject'] = subject
msg['To'] = to
msg['From'] = sent_from
msg.set_content(prepMessage)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg.as_string())
    server.close()
    print('Email sent!')

except Exception as e:
    print(e)
