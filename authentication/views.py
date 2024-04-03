from rest_framework.authtoken.models import Token

from django.shortcuts import render

# Create your views here.
#from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
#from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import UserLoginSerializer
from .serializers import CustomUserSerializer


@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    # Implement login logic here
    email = request.data.get('email')
    password = request.data.get('password')

    # Authenticate the user
    user = authenticate(email=email, password=password)

    if user is not None:
        # User is authenticated
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk}, status=status.HTTP_200_OK)
    else:
        # Authentication failed
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLoginView(ObtainAuthToken):
    serializer_class = UserLoginSerializer
# class UserLoginView(ObtainAuthToken):
#     serializer_class = UserLoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data.get('user')
        
#         token, created = Token.objects.get_or_create(user=user)

#         return Response({'token': token.key, 'user_id': user.pk}, status=status.HTTP_200_OK)