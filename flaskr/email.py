import smtplib
import ssl
from email.message import EmailMessage

def sendInvoice():
    

    email_sender = 'tomrowe76@outlook.com'
    email_password = 'password123'
    email_receiver = 'DesignServices@gmail.com'

    subject = 'Invoice'
    body = GenerateInvoice()

    em = EmailMessage()
    em['From'] = email_sender

    em['To'] = email_receiver

    em['Subject'] = subject


    em.set_content(body)




    context = ssl.create_default_context()

    #logs into email server

    with smtplib.SMTP_SSL('smtp.outlook.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())