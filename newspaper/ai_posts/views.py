from django.shortcuts import render, HttpResponse

from .models import *

from .models import *


def index(request):
    return render(request, 'ai_posts/index.html', {'title': 'Главная',})


def contacts(request):
    return render(request, 'ai_posts/contacts.html', {'title': 'Контакты'})


def mailing(request):
    return render(request, 'ai_posts/mailing.html', {'title': 'Рассылка'})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас'})


def categories(request):
    return render(request, 'ai_posts/categories.html',)


def all_posts(request, cat_id):
    category = Category.objects.filter(pk=cat_id)[0]
    posts = Post.objects.filter(post_category_id=cat_id)
    return render(request, 'ai_posts/all_posts.html', {'category': category, 'posts': posts})
