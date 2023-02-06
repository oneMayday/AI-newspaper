from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('mailing/', mailing, name='mailing'),
    # path('categories/<')
]
