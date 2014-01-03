#! /usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
def notify(from_addr, to_addrs, subject, body, mail_server)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addrs)

    server = smtplib.SMTP(mail_server)
    server.ehlo()
    server.starttls()
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()
