# coding: utf-8
# autor: Eduardo Prioli Novaes
# Sexta-feira, Junho 8 de 2018
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import filedialog, Tk
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

    # server = smtplib.SMTP('localhost')
    return server

return server

def enviar_email(destinatario, remetente, senha, server):
    # Informações da mensagem  - o tipo correto do MIME é multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Notificação para se cadastrar no Eduroam da UFRJ"
    msg['From'] = remetente
    msg['To'] = destinatario

    # Cria o corpo da mensagem.
    text = "Usuário!\nPor favor clique no link abaixo para registrar sua senha para poder usar o Eduroam da UFRJ\nhttp://localhost:8000/eduroam/hit887FDD2FFD8E9FC270217AECC89D25EC76331118\n"
    html = """\
    <html>
        <head></head>
        <body>
            <p>Usuário,<br>
            Use o link abaixo para conectar-se ao nosso site para cadastrar sua senha no Eduroam.<br>
            Aqui está o link do  <a href="http://localhost:8000/eduroam/hit887FDD2FFD8E9FC270217AECC89D25EC76331118">Eduroam</a> para cadastrar a sua senha.
            </p>
        </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    server.login(remetente,senha)
    server.sendmail(remetente, destinatario, msg.as_string())
