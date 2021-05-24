from re import I
from django.shortcuts import render

from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comments
from .serializer import CommentsSerializer





class CommentsViewSet(viewsets.ViewSet):

    def list(self, request):
        """ если  есть get параметры :
                -вывод списка коментариев по id coin
            иначе:
                -вывод списка всех  обьектов"""

        params = self.request.query_params
        if params:
            coin_id = params['coin_id']
            queryset = Comments.objects.filter(object_id=coin_id)
 
        else:
            queryset = Comments.objects.all()
        serializer = CommentsSerializer(queryset, many=True, read_only=True)
            
        return Response(serializer.data)
        
   


    def create(self, request):
        
        """ создание коментария"""

        serializer = CommentsSerializer(data=request.data,read_only=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# {
#     "text_comment": "",
#     "user_parent": null,
#     "object_id": null,
#     "user": null,
#     "parent": null,
#     "content_type": null
# }


 
