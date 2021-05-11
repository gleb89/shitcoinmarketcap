import datetime
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import string
import smtplib

from .models import Coins
from config.keysetting import config


session = Session()


def update_price_coin(coin_symbol):
    """
        get item url
    """
    name_coin = coin_symbol.lower() 
    url = f'https://api.coingecko.com/api/v3/coins/{name_coin}/'
    response = session.get(url)
    data = response.json()
    price = int(data['market_data']['current_price']['usd'])
    market_cap = int(data['market_data']['market_cap']['usd'])
    volume = int(data['market_data']['total_volume']['usd'])
    image = str(data['image']['small'])
    price_exc = int(data['market_data']['price_change_percentage_24h'])
    
    return price, market_cap, volume, image, price_exc

    

def get_update_price_coins():
    """
        update price
    """   
    for coin in Coins.objects.all():
        print((coin))
        coin.price, coin.market_cap, coin.volume, coin.image, coin.price_exc = update_price_coin(coin.name)
        coin.save()







