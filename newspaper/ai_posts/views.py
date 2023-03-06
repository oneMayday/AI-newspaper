from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from .forms import UserCreateForm, Mailing
from .services import get_all_posts_from_category, get_post, get_user_mailing_data, clear_user_mailings
from .tasks import send_mailing_confirm


class Register(View):
    """Registration form."""
    template_name = 'registration/register.html'

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('home')
        else:
            context = {
                'title': 'Регистрация',
                'form': UserCreateForm(),
            }
            return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreateForm(request.POST)

        # Checking validation:
        # if validation is True - add user to db, if False - return user to completion form page.
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('home')

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


def all_posts(request, cat_slug):
    """View for all posts in category page."""
    category, page_obj = get_all_posts_from_category(request, cat_slug)

    context = {
                'title': category.title,
                'category': category,
                'page_obj': page_obj
    }
    return render(request, 'ai_posts/all_posts.html', context)


def post(request, cat_slug, post_id):
    """View for choosen post page."""
    category, target_post = get_post(cat_slug, post_id)
    context = {
                'title': target_post.title,
                'post': target_post,
                'category': category,
    }
    return render(request, 'ai_posts/post.html', context)


def profile(request, user_id):
    """View for user profile page."""
    user = request.user
    if not user.is_authenticated:
        return redirect('register')

    mailing_list = get_user_mailing_data(user)
    context = {
                'title': 'Личный кабинет',
                'user_email': user.email,
                'mailing_list': mailing_list
    }
    return render(request, 'ai_posts/profile.html', context)


def clear_mailings(request, user_id):
    """View for clear mailings page"""
    user = request.user
    if not user.is_authenticated:
        return redirect('register')

    clear_user_mailings(user)
    return redirect('profile', user_id)


def mailing(request):
    """View for mailing page."""
    user = request.user
    if not user.is_authenticated:
        return redirect('register')

    done = ''
    if request.method == 'POST':
        mailing_form = Mailing(request.POST)
        if mailing_form.is_valid():

            # Add new users mailings, clear it
            mailing_list = get_user_mailing_data(user, mailing_form)
            send_mailing_confirm.delay(user.email, mailing_list)
            done = 'Подписка успешно оформлена!'
    else:
        mailing_form = Mailing()

    context = {'title': 'Рассылка',
               'done': done,
               'mailing_form': mailing_form,
               }
    return render(request, 'ai_posts/mailing.html', context)


def index(request):
    """View for main page."""
    return render(request, 'ai_posts/index.html', {'title': 'Главная'})


def about(request):
    """View for about page."""
    return render(request, 'ai_posts/about.html', {'title': 'О нас/Контакты'})


def categories(request):
    """View for categories page."""
    return render(request, 'ai_posts/categories.html', {'title': 'Категории'})
