from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Post
from .forms import UserCreateForm, Mailing, User
from .services import get_user_mailing_data, clear_user_mailings
from .tasks import send_mailing_confirm


class Register(View):
    """ Registration form.
    """

    template_name = 'registration/register.html'

    def get(self, request):
        """ Form view.
        """

        context = {
            'title': 'Регистрация',
            'form': UserCreateForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """ Processing entering data.
        """

        form = UserCreateForm(request.POST)

        # Checking validation:
        # if validation is True - add user to db, if False - return user to completion form page.
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


def all_posts(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Post.objects.filter(post_category_id=category.id, is_published=True).order_by('-time_create')

    # Pagination properties.
    posts_paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = posts_paginator.get_page(page_number)

    context = {
                'title': category.title,
                'category': category,
                'page_obj': page_obj
    }
    return render(request, 'ai_posts/all_posts.html', context)


def clear_mailings(request, user_id):
    user = User.objects.get(pk=user_id)
    clear_user_mailings(user)
    return redirect('profile', user_id)


def mailing(request):
    done = ''
    if request.method == 'POST':
        mailing_form = Mailing(request.POST)
        if mailing_form.is_valid():
            # Get all users mailings and clear it.
            user = request.user

            # Get user email end mailing list and send confirm email.
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


def post(request, cat_slug, post_id):
    category = get_object_or_404(Category, slug=cat_slug)
    target_post = get_object_or_404(Post, pk=post_id)

    context = {
                'title': target_post.title,
                'post': target_post,
                'category': category,
    }
    return render(request, 'ai_posts/post.html', context)


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user_email, mailing_list = get_user_mailing_data(user)

    context = {
                'title': 'Личный кабинет',
                'user_email': user_email,
                'mailing_list': mailing_list
    }
    return render(request, 'ai_posts/profile.html', context)


def index(request):
    return render(request, 'ai_posts/index.html', {'title': 'Главная'})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас/Контакты'})


def categories(request):
    return render(request, 'ai_posts/categories.html', {'title': 'Категории'})
