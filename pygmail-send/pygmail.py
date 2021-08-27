import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

## Allow less secure apps needs to be allowed in sender gmail settings
def sendMail(whofrom,receivers,cc,Subject,Message):
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login("sender@gmail.com", 'Password')
    message = MIMEMultipart("alternative")
    thetext = ""
    thehtml = Message
    part1, part2 = MIMEText(thetext, "plain"), MIMEText(thehtml, "html")
    message["Subject"] = Subject
    message["From"] = whofrom
    message["To"] = receivers
    message["Cc"] = cc
    message.attach(part1)
    message.attach(part2)
    smtpObj.sendmail(whofrom, receivers.split(";") + cc.split(";"), message.as_string())

print('sending mail...')




message = '''
<html>

    <body>
    <h1 style="color:#0af19a;">This email was sent from python</h1>
        <p>
        <strong style="color:#370c6b;">All CSS has to be inline style attributes</strong><br>
        <strong style="color:#8647d3;">to compensate for email client preproccessing</strong><br>
        <strong style="color:#474ed3;">pretty cool though</strong><br>
        
        </p>
        <br>
        <br>
    </body>
</html>
'''

sendMail(whofrom,receivers,cc,Subject,message)

print('Done')