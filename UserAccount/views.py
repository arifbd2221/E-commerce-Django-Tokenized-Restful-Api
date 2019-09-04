from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import status



from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from .serializers import UserSerializer,UpdateProfileSerializer

@csrf_exempt
@api_view(['POST',])
@permission_classes((AllowAny,))
def useregistration(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data={}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'User registration successfull'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data=serializer.errors

        return Response(data)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    print('id: '.format(request.user.id))
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):

    users = User.objects.all()
    users_serialized = serializers.serialize('json', users)
    return JsonResponse(users_serialized, safe=False)

@csrf_exempt
@api_view(["GET"])
def get_current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@csrf_exempt
@api_view(["PUT"])
def updateprofile(request):
    if request.method == 'PUT':
        print(request.data)
        # print('id: '.format(user_model.username))
        serializer = UpdateProfileSerializer(data=request.data)
        data={}

        return Response(data)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)