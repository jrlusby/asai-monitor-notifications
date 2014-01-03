#! /usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

me = 'support@asaiatm.com'
you = 'gus@asaiatm.com'

msg = MIMEText("This is a test email sent via python for use with the asai monitor program")
msg['Subject'] = "Monitor Notifications Test Email"
msg['From'] = me
msg['To'] = you

server = smtplib.SMTP('mail.asaiatm.com:587')
server.ehlo()
server.starttls()
server.sendmail(me, [you], msg.as_string())
server.quit()
