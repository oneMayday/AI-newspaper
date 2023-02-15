from django.shortcuts import render, HttpResponse

from .models import *
from .forms import *


def index(request):
    return render(request, 'ai_posts/index.html', {'title': 'Главная',})


def contacts(request):
    return render(request, 'ai_posts/contacts.html', {'title': 'Контакты'})


def mailing(request):
    if request.method == 'POST':
        mailing_form = Mailing(request.POST)
        if mailing_form.is_valid():
            print(mailing_form.cleaned_data)
    else:
        mailing_form = Mailing()

    return render(request, 'ai_posts/mailing.html', {'title': 'Рассылка', 'mailing_form': mailing_form})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас'})


def categories(request):
    return render(request, 'ai_posts/categories.html',)


def all_posts(request, cat_id):
    category = Category.objects.filter(pk=cat_id)[0]
    return render(request, 'ai_posts/all_posts.html', {'category': category})
