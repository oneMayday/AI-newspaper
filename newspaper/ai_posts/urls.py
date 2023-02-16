from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('mailing/', mailing, name='mailing'),
    path('categories/', categories, name='categories'),
    path('categories/<int:cat_id>/', all_posts, name='posts'),
]
