import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class SmtpFunc:
    def SmtpSend(mailFrom, mailTo, mailFromPass, body):
        msg = MIMEMultipart()
        msg['From'] = mailFrom
        msg['To'] = mailTo
        msg['Subject'] = 'New message(s) to your Character'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(mailFrom, mailFromPass)
        text = msg.as_string()
        server.sendmail(mailFrom, mailTo, text)
        server.quit()
