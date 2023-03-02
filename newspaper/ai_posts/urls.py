from django.urls import path, include

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('about/', about, name='about'),
    path('profile/<int:user_id>/', profile, name='account'),
    path('profile/<int:user_id>/clear-mailings/', clear_mailings, name='clear_mailings'),
    path('mailing/', mailing, name='mailing'),
    path('categories/', categories, name='categories'),
    path('categories/<int:cat_id>/', all_posts, name='posts'),
    path('categories/<int:cat_id>/<int:post_id>/', post, name='post'),
]
