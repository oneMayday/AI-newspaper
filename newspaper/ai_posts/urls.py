from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('mailing/', mailing, name='mailing'),
    path('categories/', categories, name='categories'),
    path('categories/<int:cat_id>/', all_posts, name='posts'),
]
