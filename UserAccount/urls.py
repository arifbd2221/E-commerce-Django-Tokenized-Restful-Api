from django.urls import path
from .views import *

app_name='UserAccount'

urlpatterns = [
    path('register/', useregistration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('update/profile/', updateprofile, name='profile'),
    path('allusers/', sample_api, name='api'),
    path('current/user/', get_current_user, name='currentuser'),
]