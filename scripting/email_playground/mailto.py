# Import smtplib for the actual sending function
# we need smtp server to send emails
 #simple mail transfer protocol
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Gina'
email['to'] = 'abc@gmail.com'
email['subject'] = 'Breathe, You are alive!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('@gmail.com', 'password')
    smtp.send_message(email)
    print('all good boss!')


# ===============================
# completed project code


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = '<to email address >'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)
  print('all good boss!')