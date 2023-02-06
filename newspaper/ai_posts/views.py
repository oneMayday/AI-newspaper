from django.shortcuts import render


def index(request):
    return render(request, 'ai_posts/index.html', {'title': 'Главная'})


def contacts(request):
    return render(request, 'ai_posts/contacts.html', {'title': 'Контакты'})


def mailing(request):
    return render(request, 'ai_posts/mailing.html', {'title': 'Рассылка'})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас'})
