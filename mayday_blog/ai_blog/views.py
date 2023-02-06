from django.shortcuts import render


def index(request):
    return render(request, 'ai_blog/index.html', {'title': 'Главная'})


def contacts(request):
    return render(request, 'ai_blog/contacts.html', {'title': 'Контакты'})


def mailing(request):
    return render(request, 'ai_blog/mailing.html', {'title': 'Рассылка'})


def about(request):
    return render(request, 'ai_blog/about.html', {'title': 'О нас'})
