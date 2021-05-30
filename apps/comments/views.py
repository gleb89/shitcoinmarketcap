from django.shortcuts import render

from rest_framework import  viewsets
from rest_framework.response import Response

from .models import Comments
from .serializer import CommentsSerializer


class CommentsViewSet(viewsets.ViewSet):

    def list(self, request):
        """
        если  есть get параметры :
                -вывод списка коментариев по id coin
            иначе:
                -вывод списка всех  обьектов

        """

        params = self.request.query_params
        if params:
            coin_id = params['coin_id']
            queryset = Comments.objects.filter(object_id=coin_id)

        else:
            queryset = Comments.objects.all()
        serializer = CommentsSerializer(queryset, many=True, read_only=True)

        return Response(serializer.data)

    def create(self, request):
        """ 

        создание коментария

        """

        serializer = CommentsSerializer(data=request.data, read_only=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
