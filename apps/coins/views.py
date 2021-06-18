import threading


from django.shortcuts import redirect

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

from .models import Coins, Exchange
from .service import (
                            get_market_coins,
                            update_price_coin
                            )
from .serializer import CoinsSerializer, ExchangeSerializer
from .tasks import gettts



def redirect_home_on_admin(request):
    return redirect('/api/admin/')


class CoinsPaginationViewSet(viewsets.ModelViewSet):

    queryset = Coins.objects.all().order_by('-market_cap')
    serializer_class = CoinsSerializer
    paginate_by = 1
    pagination_class = PageNumberPagination

from rest_framework.permissions import IsAuthenticated,AllowAny

class CoinsViewSet(viewsets.ViewSet):


    def list(self, request):
        """ 

        список обьектов без пагинации

        """
        # gettts.delay()
        print(request.user)
        queryset = Coins.objects.all()
        serializer = CoinsSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def update_one_data_coin(self,request,name):
        coin = Coins.objects.get(name=name)
        
        (
            coin.price,
            coin.market_cap,
            coin.volume,
            coin.image,
            coin.price_exc,
            coin.board_price
        ) = update_price_coin(name)
        coin.save()
        serializer = CoinsSerializer(coin)
        return Response(serializer.data)


snippet_list = CoinsViewSet.as_view({
    'get': 'update_one_data_coin',
    
})

class ExchangeViewSet(viewsets.ViewSet):

    def list(self, request):
        """ 

        список бирж

        """  
        # thread = threading.Thread(target=get_exchanges_list)
        # thread.start()
        
        try:
            coins_not_echange = Coins.objects.filter(market_exchange=None)
            thread = threading.Thread(target=get_market_coins(coins_not_echange))
            thread.start()
        except:
            pass 
        queryset = Exchange.objects.all()
        serializer = ExchangeSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

class CoinsNewViewSet(viewsets.ViewSet):

    def list(self, request):
        """ 

        список обьектов без пагинации

        """

        # tasks.get_update_price_coins.delay()
        # thread = threading.Thread(target=get_update_price_coins)
        # thread.start()
        
        queryset = Coins.objects.all()
        serializer = CoinsSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)


