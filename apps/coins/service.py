import datetime
import time
from requests import Session
import requests

from .models import Coins, Exchange

headers = {
  'Accepts': 'application/json'
  
}

session = Session()
session.headers.update(headers)
delay = 35000


def get_exchange(pk):
    url = f'https://api.coingecko.com/api/v3/exchanges/{pk}'
    data = session.get(url)
    print(data, pk)
    echange_db = Exchange.objects.filter(name=pk).first()
    if echange_db:
        return 
    else:
        try:
            url = f'https://api.coingecko.com/api/v3/exchanges/{pk}'
            data = session.get(url)
            response_data = data.json()
            name = response_data['name']
            image = response_data['image']
            slug = response_data['name']
            trade_url = response_data['url']
            exchange = Exchange(
                name=name,
                image=image,
                slug=slug,
                trade_url=trade_url
                )
            exchange.save()

            print('сохранено-', exchange.id)
            return exchange
        except:
            print('none')


 
def get_exchanges_list():
    counter = 0
    url = 'https://api.coingecko.com/api/v3/exchanges/list'
    response_exchanges = session.get(url)
    data = response_exchanges.json()
    for exchange in data:
        counter = counter+1
        exchange_pk = exchange['id']
        if counter== 60:
            counter = 0
            time.sleep(60)
        time.sleep(5)
        get_exchange(exchange_pk)
        


def get_chart_data(id):
    list_price_7d = {}
    days = 7
    today_date = datetime.date.today() - datetime.timedelta(days=days)
    
    while days >=1:
        url_price_7d = f'''
        https://api.coingecko.com/api/v3/coins/{id}/history?date={today_date.strftime("%d-%m-%Y")}
        '''
        response_price_7d = session.get(url_price_7d)
        data_price = response_price_7d.json()
        data_price_today = int(data_price['market_data']['current_price']['usd'])
        today_date = datetime.date.today()  - datetime.timedelta(days=days-1)
        list_price_7d[str(days)]=data_price_today
        days = days - 1
    return list_price_7d


def update_price_coin(coin_symbol):
    """
        get item url
    """
    
    name_coin = coin_symbol.lower() 
    url = f'https://api.coingecko.com/api/v3/coins/{name_coin}/'
    response = session.get(url)
    data = response.json()
    price_7d = get_chart_data(coin_symbol)
    price = data['market_data']['current_price']['usd']
    market_cap = data['market_data']['market_cap']['usd']
    volume = int(data['market_data']['total_volume']['usd'])
    image = str(data['image']['small'])
    price_exc = int(data['market_data']['price_change_percentage_24h'])
    
    return price, market_cap, volume, image, price_exc, price_7d

    

def get_update_price_coins():
    """
        update price
    """ 
    while True:
        time.sleep(delay)  
        for coin in Coins.objects.all():
            print(coin)
            (
                coin.price,
                coin.market_cap,
                coin.volume,
                coin.image,
                coin.price_exc,
                coin.board_price
                ) = update_price_coin(coin.name)
            coin.save()











