from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.views import View
from django.shortcuts import render, redirect

from .models import Category, Post
from .forms import UserCreateForm, Mailing, User


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
            # print(mailing_form.cleaned_data)
            # print(request.user.email)
            # Get all users mailings and clear it
            user = request.user
            all_user_mailings = User.objects.get(pk=user.pk).mailings.all()
            user.mailings.remove(*all_user_mailings)
            a = []
            for cat in mailing_form.cleaned_data.get('mailing_categories'):
                user.mailings.add(cat)

            res = User.objects.get(pk=user.pk).mailings.all()
            res_text = [elem.title for elem in res]
            message_text = ', '.join(res_text)
            print(res_text)
            print(a)
            subject = 'Пробное сообщение'
            message = f'Вы подписались на категории: {message_text}'
            email = EmailMessage(subject, message, to=['def@domain.com'])
            email.send()
            done = 'Подписка успешно оформлена!'
            # try:
            #     send_mail(subject, message, 'webmaster@localhost', ['webmaster@localhost'])
            # except BadHeaderError:
            #     return HttpResponse('Найден некорректный заголовок')
            # return redirect('home')
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
    category = Category.objects.filter(pk=cat_id)[0]
    return render(request, 'ai_posts/all_posts.html', {'title': category.title, 'category': category})


def profile(request, user_id):
    return render(request, 'ai_posts/profile.html', {'title': 'Личный кабинет'})


def post(request, cat_id, post_id):
    category = Category.objects.filter(pk=cat_id)[0]
    target_post = Post.objects.filter(pk=post_id)[0]

    context = {
        'title': target_post.title,
        'post': target_post,
        'category': category,
    }
    return render(request, 'ai_posts/post.html', context)
