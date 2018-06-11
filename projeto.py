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
    for destinatario in lista_emails:
        enviar_email(destinatario, remetente, senha, server)
    server.quit()
    print('Foi enviado notificação via email para os seguintes endereços eletrônicos:')
    print(lista_emails)

main()
