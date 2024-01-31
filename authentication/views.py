#create views.py

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
# from pyparsing import Token

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .serializers import UserSerializer
from rest_framework import status
# from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes


@api_view(['POST'])
def login(request):
    user = User.objects.get(username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'message': 'Wrong password'}, status=status.HTTP_200_OK)
    
    token = Token.objects.get(user=user)
    
    #remove the password on the return
    return Response({'token': token.key, 'user': UserSerializer(user).data})

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")
