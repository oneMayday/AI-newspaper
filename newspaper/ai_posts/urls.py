from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('mailing/', mailing, name='mailing'),
    path('categories/', show_categories, name='categories'),
    path('categories/<int:category_id>/', show_cat_posts, name='cat_posts'),
    # path('categories/<int:category_id/post/<int:post_id>', show_post, name='post'),

]
