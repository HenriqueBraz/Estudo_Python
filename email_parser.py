# email_parser - python 3.7

import imapclient
import imaplib
import pyzmail


server_name = 'gmail'
type_search = False   #'True' to search using Gmail’s X-GM-RAW attribute. http://nostarch.com/automatestuff/
password = 'XXXXXX'
server_login = 'testeblisk999@gmail.com'
messages = {}
message = ''

try:
    if server_name == 'gmail':

        imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

    elif server_name == 'outlook':
        
       imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)

    elif server_name == 'yahoo':
        
        imapObj = imapclient.IMAPClient('imap.mail.yahoo.com', ssl=True)

    elif server_name == 'att':
        
        imapObj = imapclient.IMAPClient('imap.mail.att.net', ssl=True)


    elif server_name == 'comcast':

        imapObj = imapclient.IMAPClient('imap.comcast.ne', ssl=True)

    elif server_name == 'verzion':
        
        imapObj = imapclient.IMAPClient('incoming.verizon.net', ssl=True)


    else:
        print('erro ao identificar o servidor')


except Exception as e:
    print('Erro de conexão: ' + str(e))

try:
    imapObj.login(server_login,password)
    imapObj.select_folder('INBOX', readonly=False)

    if type_search:
        UIDs = imapObj.gmail_search('is: unread in: inbox') #search do google, funciona apenas para server == gmail


    else:
        UIDs = imapObj.search(['UNSEEN'])  #UNSEEN, ALL,

    try:
        imaplib._MAXLINE = 10000000  # define o armazenamento máximo de menssagens ( mas nao limitado a ) em 10Mb
        rawMessages = imapObj.fetch(UIDs,['BODY[]','FLAGS']) #cria um dicionario com emails e marca como lido no servidor
        imapObj.logout()
    except Exception as e:
        print('Erro em baixar emails ou encerrar conexão: '+str(e))

    for i in UIDs:
        message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])#Salva o conteudo em forma de objeto PyzMessages
        print('From: ' +str(message.get_addresses('from')))
        print('To: ' + str(message.get_addresses('to')))
        print('Cc: ' + str(message.get_addresses('cc')))
        print('Bcc:' + str(message.get_addresses('bcc')))
        print('Subject: ' + str(message.get_subject()))
        print('Body: ' + message.text_part.get_payload().decode('utf-8'))

except Exception as e:
    print('Erro: '+str(e))
