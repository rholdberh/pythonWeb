#!/usr/bin/python
import smtplib
from email.message import EmailMessage


class Mail:

    def __init__(self):
        self.gmail_user = 'r.holdberh@gmail.com'
        self.gmail_password = ''

    def send_mail(self, message_body, message_subject, send_to):
        for rec in send_to:
            self.send(message_body, message_subject,rec)

    def send(self, message_body, message_subject, send_to):
        print(self.gmail_user)
        print(send_to)
        sent_from = self.gmail_user
        subject = message_subject

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['To'] = send_to
        msg['From'] = sent_from
        msg.set_content(message_body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(sent_from, send_to, msg.as_string())
            server.close()
            print('Email sent')
            return True
        except Exception as e:
            print('error')
            print(e)
            return False
