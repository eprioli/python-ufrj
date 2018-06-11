# coding: utf-8
# autor: Eduardo Prioli Novaes
# Sexta-feira, Junho 8 de 2018
#!/usr/bin/env python3

# Esse projeto é para envio de emails com Python
# Vai ler de um arquivo txt os endereços de emails e irá enviar um email de
# notificação para cada um deles.



import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from func import *
from credenciais import *

# Credenciais
remetente    = getLogin()
senha        = getSenha()


def main():
    nome_arquivo = pede_arquivo()
    lista_emails = abre_arquivoCVS(nome_arquivo)
    server = bootstrapServer()
    print('Inicio do envio de e-mails')
    print('')
    print('')

    for dados in lista_emails:
        try:
            enviar_email(dados, remetente, senha, server)
            print("Enviado - OK ***********" + dados[0] + " - " + dados[1])
        except Exception as e:
            print("Enviado - ERRO *********" + dados[0] + " - " + dados[1])
    server.quit()
    
    print('')
    print('')
    print('Fim do envio de e-mails')


main()
