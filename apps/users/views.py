from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
