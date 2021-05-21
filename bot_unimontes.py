import time
import tweepy
import datetime
from pytz import timezone

DT_FIM = '05/07/2021'
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACESS_TOKEK_SECRET = ''


def conta_dias():
    data_atual = datetime.datetime.now()
    fuso = timezone('America/Sao_Paulo')
    data_atual_com_fuso = data_atual.astimezone(fuso)
    data_em_texto = data_atual_com_fuso.strftime('%d/%m/%Y')
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


def main():
    sleep = int(86400)
    while 1:
        text = create_tweet()
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEK_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            api.update_status(text)
            # print(text)
            # print(datetime.datetime.now())
        except tweepy.TweepError as e:
            print(f'Erro: {e}')

        time.sleep(sleep)


if __name__ == '__main__':
    main()



