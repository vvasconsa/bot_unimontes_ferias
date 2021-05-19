import time
import tweepy
from datetime import date
import datetime

DT_FIM = '05/07/2021'
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACESS_TOKEK_SECRET = ''


def conta_dias():
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    date1 = datetime.datetime.strptime(data_em_texto, '%d/%m/%Y')
    date2 = datetime.datetime.strptime(DT_FIM, '%d/%m/%Y')
    quantidade_dias = abs((date2 - date1).days)
    return quantidade_dias


def create_tweet():
    x = conta_dias()
    if x == 0:
        y = 'Finalmente é férias!!! IRIRIRIIIIIII!! (Exceto se tu tomou final então vai estudar!)'
    else:
        y = f'Faltam {conta_dias()} dias para o fim do semestre letivo!'
    return y


def hora_de_tweetar():
    data_e_hora_atuais = datetime.datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M')
    return data_e_hora_em_texto


text = create_tweet()


while 1:
    print(text)
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEK_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.update_status(text)
    except tweepy.TweepError as e:
        print(e.reason)
    time.sleep(43200)




