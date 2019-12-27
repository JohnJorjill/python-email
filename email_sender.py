import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'John Jorjill'
email['to'] = 'orgil9506@gmail.com'
email['subject'] = 'Hello there!'

email.set_content(html.substitute(name='John'),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('orgil9506@gmail.com','')
	smtp.send_message(email)
	print('email is sent')