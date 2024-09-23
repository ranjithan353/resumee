import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender-email="ranju.gowda@143666gmail.com"
receiver_email="sumanthpss07@gmai.com"
password="ranju@353"
subject='test email'
body = "this is a test email sent from python"
message=MIMEMultipart()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]=subject
message.attach(MIMEText(body,"plain"))
smpt_server="smpt.gmail.com"
port=587
try:
    server=smtplib.SMTP(smtp_server,port)
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())
    print("Email sent successfully!")
except Exception as e:
     print(f"error:{e}")

finally:
    server.quit()
