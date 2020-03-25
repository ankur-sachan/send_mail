import smtplib
import os
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders


## Created msg here # define From To and 
msg=MIMEMultipart()
msg['Subject'] = 'Hey ceckout my new mail'
msg['From'] = "Learning@hireme.com"
msg['To'] = "hr1@hired.com,hr2@hired.com"

msg.preamble="Send python"
Output_file=r"C:\Users\ankur\OneDrive\Desktop\ankur.py.txt"

## body of a mail
body="this content will appear in mails body"
#adding body to msg
msg.attach(MIMEText(body,"plain"))

## preparation of attachement
part =MIMEBase('application', "octet-stream")
part.set_payload(open(Output_file,"rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachement; filename="%s"' % os.path.basename(Output_file))

# adding part/attachment in msg
msg.attach(part)
try:
    s=smptlib.SMTP("mailhost.ldn.bank.com")
    s.sendmail(msg['From'],msg['To'].split(",") , msg.as_string())
    s.quit()
    print("mailsent")
except:
    print("Connection issue, check with L3")
