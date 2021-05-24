from django.contrib.auth.models import User, Group
from rest_framework import serializers


from .models import Coins, Exchange, Note
from apps.comments.models import Comments
from apps.comments.serializer import CommentsSerializer
from apps.comments.models import Comments
from apps.comments.serializer import  CommentsSerializer





class ExchangeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exchange
        fields = ['id', 'name','slug']


class CoinsSerializer(serializers.ModelSerializer):
    """ Coin Коментарий"""
    class Meta:
        model = Coins
        fields = '__all__'
        depth = 1




