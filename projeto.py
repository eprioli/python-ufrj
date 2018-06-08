# coding: utf-8

# Esse projeto é para envio de emails com Python
# Vai ler de um arquivo txt os endereços de emails e irá enviar um email de
# notificação para cada um deles.

import smtplib

from func import *
from credenciais import *

# Credenciais
remetente    = getLogin()
senha        = getSenha()

def main():
    nome_arquivo = pede_arquivo()
    lista_emails = abre_arquivo(nome_arquivo)
    server = bootstrapServer()
    for destinatario in lista_emails:
        enviar_email(destinatario, remetente, senha, server)
    server.close()
    print('Foi enviado notificação via email para os seguintes endereços eletrônicos:')
    print(lista_emails)

main()
