import logging
import smtplib
import zipfile
import time
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


DATE_THUMBS ='{0:%d-%m-%Y}'.format(datetime.datetime.now())
DATE_SEND= datetime.datetime.now()


def sendEmail():
    zf = open("/path/to/file.zip".format(DATE_THUMBS),'rb')
    msg = MIMEMultipart()
    recipients = ['email@domain1','email@domain2']
    msg['From'] = 'email@domain'
    msg['To'] = ", ".join(recipients)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = 'Subject_text {}'.format(DATE_THUMBS)
    msg.attach (MIMEText('Segue em anexo thumbnails gerados automaticamente.'))
    part = MIMEBase('application', "octet-stream")
    part.set_payload(zf.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="/paht/to/file_{}.zip"'.format(DATE_THUMBS))
    msg.attach(part)
    error_log = open("/opt/scripts/sendEmail.log","w")
    try:
        server = smtplib.SMTP('ip_server:25')
        server.ehlo()
        server.sendmail('email@domain', recipients , str(msg))
        server.close()
        with open("/opt/scripts/sendEmail.log","a") as arquivo_log:
             arquivo_log.write('successfully sent the mail at {} \n'.format(str(DATE_SEND)))
             arquivo_log.close()
        print ('successfully sent the mail')
    except Exception as err:
        print(str(err))
def main():
    textMessage = '''
        Email from a script
        The information in here is
        a zip file.
    '''

    sendEmail()



if __name__ == '__main__':
    main()

