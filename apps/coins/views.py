from django.http import HttpResponse
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Coins
from .serializer import  CoinsSerializer
from .service import get_update_price_coins



class CoinsPaginationViewSet(viewsets.ModelViewSet):
    get_update_price_coins()
    queryset = Coins.objects.all().order_by('id')
    serializer_class = CoinsSerializer
    paginate_by = 1
    pagination_class = PageNumberPagination





class CoinsViewSet(viewsets.ViewSet):


    def list(self, request):

        """ список обьектов"""
        print(request.user.username)
        queryset = Coins.objects.all()
        serializer = CoinsSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

 


