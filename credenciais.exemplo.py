# coding: utf-8
# autor: Eduardo Prioli Novaes
# Sexta-feira, Junho 8 de 2018
import smtplib

def getLogin():
    return 'o email do desenv aqui'

def getSenha():
    return 'no_need_to_put_your_secret_password_since_we_do_not_use_it'

def getServidor():
    return smtplib.SMTP('IP_SERVIDOR_EMAIL:PORTA')
