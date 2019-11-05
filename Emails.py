from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

#mime: multipurpose internet mail extensions

message = MIMEMultipart()
message["from"] = "The Syndicate"
message["to"] = "aasdfghfyi@yahoo.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
#message.attach(MIMEImage(Path("mosh.png").read_bytes()))

with smtplib.SMTP(host="smtp.yahoo.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("aasdfghfyi@yahoo.com", "DTjh43676!")
    smtp.send_message(message)
    print("sent...")