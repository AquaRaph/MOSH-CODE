from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

#mime: multipurpose internet mail extensions
template = Template(Path("Template.html").read_text())




message = MIMEMultipart()
message["from"] = "The Syndicate"
message["to"] = "aasdfghfyi@yahoo.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
#message.attach(MIMEImage(Path("mosh.png").read_bytes()))

with smtplib.SMTP(host="smtp.yahoo.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("aasdfghfyi@yahoo.com", "DTjh43676!")
    smtp.send_message(message)
    print("sent...")