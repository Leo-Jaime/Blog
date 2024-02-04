import smtplib
import os

USER = os.environ.get('USER_EMAIL')
SENHA = os.environ.get('USER_SENHA')
EMAIL_DESTINO = os.environ.get('EMAIL_DETINO')
def enviar_email(mensagem):
    conexao = smtplib.SMTP("smtp.gmail.com")
    conexao.starttls()
    conexao.login(user=USER, password=SENHA)
    conexao.sendmail(USER, EMAIL_DESTINO, mensagem)
    conexao.quit()
