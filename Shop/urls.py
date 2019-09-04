from django.urls import path
from .views import allproducts,productdetails

urlpatterns = [
    path('list/', allproducts, name='products'),
    path('details/<int:id>/', productdetails, name='details'),
]