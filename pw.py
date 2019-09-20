#! /usr/bin/python3
# -*- coding: utf-8 -*-
# pw.py – Um programa para repositório de senha que não é seguro.
import sys
import pyperclip


PASSWORDS = {'testeblisk2@gmail.com': 'xxxxxxx','testeblisk@kangurunet.com.br': 'xxxxxxx'}

if len(sys.argv) < 2:
    print('\nOpções:\n')
    print('digite: ./pw.py [conta] -> copia a senha da conta digitada para o clipboard (área de transferência).\n')
    print('digite: ./pw.py [listar] -> ver as contas cadastradas\n')
    sys.exit()
    
    
account = sys.argv[1] # o primeiro argumento da linha de comando é o nome da conta

if account == 'listar':
    print('contas cadastradas:\n')
    for k in PASSWORDS.keys():
      print(k)
    print('\n')

elif account in PASSWORDS:
    text = PASSWORDS[account]
    pyperclip.copy(text)
    print('Senha de ' + account + ' copiado para o clipboard (área de transferência).')
    
else:
    print('Não há uma conta chamada ' + account)
