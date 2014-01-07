#! /usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
class Notifier:
    def __init__(self, mail_server, username, password):
        self.mail_server = mail_server
        self.username = username
        self.password = password

    def notify(self, from_addr, to_addrs, subject, body):
        server = smtplib.SMTP(self.mail_server)
        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = ', '.join(to_addrs)
        server.sendmail(from_addr, to_addrs, msg.as_string())
        server.quit()
