import threading

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Coins, Exchange
from .service import get_update_price_coins, get_exchanges_list
from .serializer import CoinsSerializer, ExchangeSerializer


class CoinsPaginationViewSet(viewsets.ModelViewSet):

    queryset = Coins.objects.all().order_by('-market_cap')
    serializer_class = CoinsSerializer
    paginate_by = 1
    pagination_class = PageNumberPagination


class CoinsViewSet(viewsets.ViewSet):

    def list(self, request):
        """ 

        список обьектов без пагинации

        """

        queryset = Coins.objects.all()
        serializer = CoinsSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)


class ExchangeViewSet(viewsets.ViewSet):

    def list(self, request):
        """ 

        список бирж

        """
        thread = threading.Thread(target=get_exchanges_list)
        thread.start()
        
        queryset = Exchange.objects.all()
        serializer = ExchangeSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

thread = threading.Thread(target=get_update_price_coins)
thread.start()
