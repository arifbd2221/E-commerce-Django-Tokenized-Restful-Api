from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from django.core import serializers
from .models import Product


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def allproducts(request):

    products = Product.objects.all()
    products_serialized = serializers.serialize('json', products)
    return JsonResponse(products_serialized, safe=False)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def productdetails(request, id):
    product = Product.objects.filter(id=id).only()
    print(product)
    product_serialized = serializers.serialize('json', product)
    return JsonResponse(product_serialized, safe=False)