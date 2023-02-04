from django.shortcuts import render


def index(request):
    return render(request, 'ai_blog/index.html')


def contacts(request):
    return render(request, 'ai_blog/contacts.html')


def mailing(request):
    return render(request, 'ai_blog/mailing.html')


def about(request):
    return render(request, 'ai_blog/about.html')
