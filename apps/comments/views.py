from django.shortcuts import render

from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from .models import Comments
from .serializer import CommentsSerializer, CommentsPostSerializer


class CommentsViewSet(viewsets.ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentsPostSerializer
    # # permission_classes = (IsAuthenticated,)
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
            queryset = Comments.objects.filter(object_id=coin_id).order_by('-updated')

        else:
            queryset = Comments.objects.all().order_by('updated')
        serializer = CommentsSerializer(queryset, many=True, read_only=True)

        return Response(serializer.data)

    # def create(self, request):
    #     """ 

    #     создание коментария

    #     """
    
    #     serializer = CommentsPostSerializer(data=request.data, many=True,read_only=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
        
 




