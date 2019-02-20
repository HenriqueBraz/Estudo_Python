# email_sender - python3.7

import smtplib

smtpObj = ''
tls = False
provider_name = 'gmail'
subject = 'Testando'
menssagem = 'Este é um teste melhorado, utilizando caracteres utf -8 <> %$#@~ççç)'
from_adrr = 'testeblisk999@gmail.com'
to_adrr = ['niyov@webmail24.top', 'testeblisk999@gmail.com']


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
    msg = 'Subject:' + subject + ' \n' + menssagem
    print(smtpObj.sendmail(from_adrr,to_adrr,msg.encode('utf-8')))
    print(smtpObj.quit())

except Exception as e:
    print('Erro: ' + str(e))