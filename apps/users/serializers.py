from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_email = User.objects.filter(username=validated_data['email'])
        
        if user_email:
            return ''
        else:
            password = validated_data.pop('password')
            user = User(username = validated_data['email'],email=validated_data['email'])
            user.set_password(password)
            user.save()
     
            return user
