from django.shortcuts import render, HttpResponse

from .models import *


def index(request):
    return render(request, 'ai_posts/index.html', {'title': 'Главная'})


def contacts(request):
    return render(request, 'ai_posts/contacts.html', {'title': 'Контакты'})


def mailing(request):
    return render(request, 'ai_posts/mailing.html', {'title': 'Рассылка'})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас'})


def show_categories(request):
    cats = Category.objects.all()
    return render(request, 'ai_posts/categories.html', {'categories': cats})


def show_cat_posts(request, category_id):
    category = Category.objects.filter(pk=category_id)[0].title
    posts = Post.objects.filter(post_category_id=category_id)
    return render(request, 'ai_posts/all_posts.html', {'posts': posts, 'category': category})


def show_post(request):
    pass
