import datetime
import time
from requests import Session


from .models import Coins, Exchange

headers = {
    'Accepts': 'application/json'

}

session = Session()
session.headers.update(headers)
delay = 4500



def save_exchange(pk):
    
    url = f'https://api.coingecko.com/api/v3/exchanges/{pk}'
    data = session.get(url)
    response_data = data.json()
    name = response_data['name'].lower()
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
    print('сохранено-', exchange.name)
    return exchange



def get_exchange(pk):

    """
        get exchange data for name exchange
    """

    url = f'https://api.coingecko.com/api/v3/exchanges/{pk}'
    data = session.get(url)
    print(data, pk)
    echange_db = Exchange.objects.filter(name=pk).first()
    if echange_db:
        return 
    else:
        try:
            return save_exchange(pk)
        except:
            print('none')




def get_exchanges_list():

    """
        get names list coins all 
    """
    counter = 0
    url = 'https://api.coingecko.com/api/v3/exchanges/list'
    response_exchanges = session.get(url)
    data = response_exchanges.json()
    for exchange in data:
        counter = counter+1
        exchange_pk = exchange['id']
        print(counter)  
        time.sleep(2)  
        get_exchange(exchange_pk)




def get_chart_data(id):

    """
        history data (price 7d) coin name
    """

    list_price_7d = {}
    days = 7
    today_date = datetime.date.today() - datetime.timedelta(days=days)

    while days >= 1:
        url_price_7d = f'''
        https://api.coingecko.com/api/v3/coins/{id}/history?date={today_date.strftime("%d-%m-%Y")}
        '''
        response_price_7d = session.get(url_price_7d)
        data_price = response_price_7d.json()
        data_price_today = int(
            data_price['market_data']['current_price']['usd'])
        today_date = datetime.date.today() - datetime.timedelta(days=days-1)
        list_price_7d[str(days)] = data_price_today
        days = days - 1
    return list_price_7d




def update_price_coin(coin_symbol):

    """
        get name_coin  url
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
        update price coin
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
            time.sleep(4)



def add_market_for_coin(market_id, coin):

    """
        add many to many Exchange for coin
    """

    exchange = Exchange.objects.filter(name=market_id).first()
    print(exchange, market_id)
    if not exchange:
        try:
            new_exchange = save_exchange(market_id)
            coin.market_exchange.add(new_exchange)
        except:
            print('error')
    else:
        print('add')
        coin.market_exchange.add(exchange)




def get_market_coins(coins):

    """
        get markets for coin id
    """

    for coin in coins:
        url = f'https://api.coingecko.com/api/v3/coins/{coin}/tickers'
        response = session.get(url)
        data = response.json()
        for market in data['tickers']:
            print(coin)
            market_name = market['market']['identifier']
            time.sleep(2)
            add_market_for_coin(market_name.lower(), coin)
