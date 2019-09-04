from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.core import serializers


@csrf_exempt
@api_view(['POST',])
@permission_classes((AllowAny,))
def createorder(request):
    if request.method == 'POST':
        pass