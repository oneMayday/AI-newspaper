from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Post
from .forms import UserCreateForm, Mailing
from .services import get_user_mailing_data
from .tasks import send_mailing_confirm


class Register(View):
    """ Registration form. """

    template_name = 'registration/register.html'

    def get(self, request):
        """ Form view. """
        context = {
            'title': 'Регистрация',
            'form': UserCreateForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """ Processing entering data """

        form = UserCreateForm(request.POST)

        # Checking validation: if validation is True - add user to db, if False - return user to completion form page
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


def mailing(request):
    """ Mailing with a category choice. """

    done = ''
    if request.method == 'POST':
        mailing_form = Mailing(request.POST)
        if mailing_form.is_valid():
            # Get all users mailings and clear it
            user = request.user

            # Get user email end mailing list and send confirm email
            user_email, mailing_list = get_user_mailing_data(user, mailing_form)
            send_mailing_confirm.delay(user_email, mailing_list)
            done = 'Подписка успешно оформлена!'
    else:
        mailing_form = Mailing()

    context = {'title': 'Рассылка',
               'done': done,
               'mailing_form': mailing_form,
               }

    return render(request, 'ai_posts/mailing.html', context)


def index(request):
    return render(request, 'ai_posts/index.html', {'title': 'Главная'})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас/Контакты'})


def categories(request):
    return render(request, 'ai_posts/categories.html', {'title': 'Категории'})


def all_posts(request, cat_id):
    category = get_object_or_404(Category, pk=cat_id)
    return render(request, 'ai_posts/all_posts.html', {'title': category.title, 'category': category})


def profile(request, user_id):
    return render(request, 'ai_posts/profile.html', {'title': 'Личный кабинет'})


def post(request, cat_id, post_id):
    category = get_object_or_404(Category, pk=cat_id)
    target_post = get_object_or_404(Post, pk=post_id)

    context = {
        'title': target_post.title,
        'post': target_post,
        'category': category,
    }
    return render(request, 'ai_posts/post.html', context)
