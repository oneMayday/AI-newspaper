from django.core.mail import send_mail

from time import sleep
from celery import shared_task, Celery

from .forms import User
from .models import Category, Post
from .chatgpt_services import chatgpt_get_post


app = Celery()


@shared_task()
def send_mailing_confirm(user_email, mailing_list):
	""" Sends and email when the mailing form has been submitted """

	sleep(5)
	send_mail(
		'Подписка оформлена (ALT_stories)',
		f'Вы подписались на категории: {mailing_list}',
		'django-mayday@mail.ru',
		[user_email],
	)


@shared_task()
def check_pr():
	print('check complete!')


@shared_task
def test(arg):
	print(arg)


def update_news():
	categories = Category.objects.all()
	for category in categories:
		post_title, post_text = chatgpt_get_post(category)

		new_post = Post(
			title=post_title,
			text=post_text,
			post_category=category.pk,
			is_published=False
		)
		new_post.save()
		sleep(120)


@shared_task()
def test_add_cat():
	categories = Category.objects.all()
	for category in categories:

		new_post = Post(title='test_title', text='test_text', post_category=category, is_published=False)
		new_post.save()
		sleep(3)