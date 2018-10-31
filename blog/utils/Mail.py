#!/usr/bin/python
import smtplib
from email.message import EmailMessage


class Mail:

    def __init__(self, message_body, message_subject):
        self.message_body = message_body
        self.message_subject = message_subject
        self.gmail_user = 'r.holdberh@gmail.com'
        self.gmail_password = ''

    def send_mail(self, send_to):
        sent_from = self.gmail_user
        to = send_to
        subject = self.message_subject

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['To'] = to
        msg['From'] = sent_from
        msg.set_content()

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(sent_from, to, msg.as_string())
            server.close()
            return True
        except Exception as e:
            print(e)
            return False
