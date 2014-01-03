#! /usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
class Notifier:
    def __init__(self, mail_server, username, password):
        self.server = smtplib.SMTP(mail_server)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(username, password)

    def __del__(self):
        self.server.quit()

    def notify(self, from_addr, to_addrs, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = ', '.join(to_addrs)
        self.server.sendmail(from_addr, to_addrs, msg.as_string())
