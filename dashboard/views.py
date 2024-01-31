from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Create your views here.
# dashboard/views.py
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def dashboard(request):
    # Your view logic for the protected dashboard view
    return Response("This is a protected dashboard view.")



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_dashboard(request):
    return Response({'message': 'Testing testing 123.'})

@api_view(['GET'])
def index(request):
    return Response({'message': 'Testing testing asdfadfasdf.'})  