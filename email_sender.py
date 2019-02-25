# email_sender - python3.7

import smtplib
import  email.mime.multipart
import email.mime.text


smtpObj = ''
tls = False
provider_name = 'gmail'
fromaddr = 'testeblisk999@gmail.com'
toaddr = 'testeblisk@999gmail.com'
msg = email.mime.multipart.MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Python email_sender test'
body = 'Este é um teste melhorado, utilizando caracteres  <> ^~^~^~%$#@~ççç)'
msg.attach(email.mime.text.MIMEText(body, 'plain'))


try:
    if provider_name == 'gmail':

        if smtplib.SMTP('smtp.gmail.com', 587):
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            tls = True

        else:
            smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)


    elif provider_name == 'outlook':
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        tls = True

    elif provider_name == 'yahoo':
        smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        tls = True

    elif provider_name == 'att':
        smtpObj = smtplib.SMTP_SSL('smtp.mail.att.net', 465)


    elif provider_name == 'comcast':
        smtpObj = smtplib.SMTP('smtp.comcast.net', 587)
        tls = True

    elif provider_name == 'verzion':
        smtpObj = smtplib.SMTP_SSL('smtp.verizon.net', 465)


    else:
        print('erro ao identificar o provedor')

except Exception as e:
    print('Erro de conexão: ' + str(e))

try:
    smtpObj.ehlo()
    if tls:
        smtpObj.starttls()
    smtpObj.login('testeblisk999@gmail.com', '123qwe.1')
    text = msg.as_string()
    smtpObj.sendmail(fromaddr, toaddr, text)
    print(smtpObj.quit())

except Exception as e:
    print('Erro: ' + str(e))