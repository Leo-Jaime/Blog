import smtplib
import os

USER = os.environ.get('USER_EMAIL')
SENHA = os.environ.get('USER_SENHA')

def enviar_email(email, mensagem):
    conexao = smtplib.SMTP("smtp.gmail.com")
    conexao.starttls()
    conexao.login(user=USER, password=SENHA)
    conexao.sendmail(USER, email, mensagem)
    conexao.quit()
