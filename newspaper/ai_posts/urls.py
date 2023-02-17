from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('about/', about, name='about'),
    path('account/<int:user_id>/', account, name='account'),
    path('mailing/', mailing, name='mailing'),
    path('categories/', categories, name='categories'),
    path('categories/<int:cat_id>/', all_posts, name='posts'),
    path('categories/<int:cat_id>/<int:post_id>', post, name='post'),
]
