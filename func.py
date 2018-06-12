# coding: utf-8
# autor: Eduardo Prioli Novaes
# Sexta-feira, Junho 8 de 2018
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import filedialog, Tk
from credenciais import *

# Credenciais
remetente    = getLogin()
senha        = getSenha()
server       = getServidor()

def pede_arquivo():
    # retorna o caminho para um arquivo definido pelo usuario
    root = Tk()
    root.withdraw() #para fechar a janela que no windows abre vazia
    return filedialog.askopenfilename()

def abre_arquivo(nome_arquivo):
    # retrona uma lista com as linhas do arquivo
    lista_linhas = []
    with open(nome_arquivo, 'r') as lista:
        for linha in lista:
            lista_linhas.append(linha.strip())
    return lista_linhas

def abre_arquivoCVS(nome_arquivo):
    lista_linhas = []
    with open(nome_arquivo) as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            lista_linhas.append(row)
    return lista_linhas

def bootstrapServer():
    # server = smtplib.SMTP('smtp.gmail.com:587')
    # server.starttls()
    return server

def enviar_email(dados, remetente, senha, server):
    nome_destinatario = dados[0]
    email_destinatario = dados[1]
    token = dados[2]

    # Informações da mensagem  - o tipo correto do MIME é multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Notificação para se cadastrar no Eduroam da UFRJ"
    # msg['From'] = remetente
    msg['To'] = email_destinatario
    link = "<a href=http://localhost:8000/eduroam/hit" + token +">Clique aqui para se cadastrar no Eduroam</a> "
    # simpleLink = "<a href=http://localhost:8000/eduroam/>http://localhost:8000/eduroam/</a> "

    # Cria o corpo da mensagem.
    text = nome_destinatario + "\nPor favor, Use o link abaixo para cadastrar-se no Eduroam da UFRJ\n" + link
    html = """\
    <html>
        <head></head>
        <body>
            <p>""" + nome_destinatario + """, <br><br><br>
            Use o link abaixo para cadastrar-se no Eduroam da UFRJ.<br>
            <br>""" + link + """<br><br><br>
            Caso não consiga clicar no link acima, por favor use o token e a uri abaixo para acessar sua página de cadastro.
            <br><br>http://localhost:8000/eduroam/<br><br>""" + token + """<br><br>
            Cordialmente,<br><br>
            Equipe do CISI<br><br>
            </p>
        </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    # server.login(remetente,senha)
    server.sendmail(remetente, email_destinatario, msg.as_string())
