# Este programa vai abrir uma planilha, ler a primeira coluna e salvar a media, mediana e o numero de linhas em um arquivo txt
from tkinter import filedialog, Tk
from time import sleep
import smtplib

def pede_arquivo():
    # retorna o caminho para um arquivo definido pelo usuario
    root = Tk()
    # root.withdraw() '''para fechar a janela que no windows abre vazia'''
    return filedialog.askopenfilename()

def abre_arquivo(nome_arquivo):
    # retrona uma lista com as linhas do arquivo
    lista_linhas = []
    with open(nome_arquivo, 'r') as lista:
        for linha in lista:
            lista_linhas.append(linha.strip())
    return lista_linhas

def bootstrapServer():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    return server

def enviar_email(destinatario, remetente, senha, server):
    # Informações da mensagem
    destinatario = destinatario
    assunto      = 'Enviando email com python'
    texto        = 'Esse email foi enviado usando python! :)'

    # Preparando a mensagem
    msg = '\r\n'.join([
      'From: %s' % remetente,
      'To: %s' % destinatario,
      'Subject: %s' % assunto,
      '',
      '%s' % texto
      ])

    # Enviando o email
    server.login(remetente,senha)
    server.sendmail(remetente, destinatario, msg)
