# Import smtplib for the actual sending function
# we need smtp server to send emails
 #simple mail transfer protocol
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'brain'
email['to'] = 'abc@gmail.com'
email['subject'] = 'You won 1,000,000,000 dollars'

email.set_content('I am a python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    #encryption method
    smtp.starttls()
    smtp.login('abc@gmail.com', 'password')
    smtp.send_message(email)
print('all good boss!')
