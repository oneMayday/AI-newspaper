from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from .models import Category, Post
from .forms import UserCreateForm, Mailing


class Register(View):
    """ Класс регистрации пользователя """
    template_name = 'registration/register.html'

    def get(self, request):
        """ Представление формы """
        context = {
            'title': 'Регистрация',
            'form': UserCreateForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """ Обработка данных, введенных в форму """
        form = UserCreateForm(request.POST)

        # Проверка валидации - если прошла - добавляем юзера в БД, если нет - возвращаем на страницу ввода:
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


def index(request):
    return render(request, 'ai_posts/index.html', {'title': 'Главная',})


def mailing(request):
    """ Рассылка, с выбором категорий"""
    if request.method == 'POST':
        mailing_form = Mailing(request.POST)
        if mailing_form.is_valid():
            print(mailing_form.cleaned_data)
    else:
        mailing_form = Mailing()
    return render(request, 'ai_posts/mailing.html', {'title': 'Рассылка', 'mailing_form': mailing_form})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас/Контакты'})


def categories(request):
    return render(request, 'ai_posts/categories.html', {'title': 'Категории'})


def all_posts(request, cat_id):
    category = Category.objects.filter(pk=cat_id)[0]
    return render(request, 'ai_posts/all_posts.html', {'title': category.title, 'category': category})


def profile(request, user_id):
    return render(request, 'ai_posts/profile.html', {'title': 'Личный кабинет'})


def post(request, cat_id, post_id):
    category = Category.objects.filter(pk=cat_id)[0]
    post = Post.objects.filter(pk=post_id)[0]
    return render(request, 'ai_posts/post.html', {'title': post.title, 'post': post, 'category': category})
