from django.shortcuts import render, HttpResponse

from .models import *

from .models import *


def index(request):
    categories = Category.objects.all()
    return render(request, 'ai_posts/index.html', {'title': 'Главная', 'categories': categories})


def contacts(request):
    return render(request, 'ai_posts/contacts.html', {'title': 'Контакты'})


def mailing(request):
    return render(request, 'ai_posts/mailing.html', {'title': 'Рассылка'})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас'})


<<<<<<< HEAD
def show_categories(request):
=======
def categories(request):
>>>>>>> feat/post-temp
    cats = Category.objects.all()
    return render(request, 'ai_posts/categories.html', {'categories': cats})


<<<<<<< HEAD
def show_cat_posts(request, category_id):
    category = Category.objects.filter(pk=category_id)[0].title
    posts = Post.objects.filter(post_category_id=category_id)
    return render(request, 'ai_posts/all_posts.html', {'posts': posts, 'category': category})


def show_post(request):
    pass
=======
def all_posts(request, cat_id):
    category = Category.objects.filter(pk=cat_id)[0]
    posts = Post.objects.filter(post_category_id=cat_id)
    return render(request, 'ai_posts/all_posts.html', {'category': category, 'posts': posts})
>>>>>>> feat/post-temp
