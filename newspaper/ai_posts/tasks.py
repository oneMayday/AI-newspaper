from django.core.mail import send_mail

from time import sleep
from celery import shared_task

from .forms import User
from .models import Category, Post
from .chatgpt_services import chatgpt_get_post
from .services import get_new_posts


@shared_task()
def send_mailing_confirm(user_email, mailing_list):
	""" Sends email when the mailing form has been submitted. """

	sleep(5)
	send_mail(
			'Подписка оформлена (ALT_stories)',
			f'Вы подписались на категории: {mailing_list}',
			'django-mayday@mail.ru',
			[user_email],
	)


@shared_task()
def send_mailing_update_news(user_email):
	""" Sends email when after creating and publishing new posts. """

	send_mail(
			'ALT_stories',
			f'Для Вас появились новые посты!\nЗайдите на сайт, чтобы посмотреть',
			'django-mayday@mail.ru',
			[user_email],
	)


@shared_task()
def update_news():
	""" Generate new posts with a chatGPT"""

	categories = Category.objects.all()

	for category in categories:
		post_title, post_text = chatgpt_get_post(category)

		new_post = Post(
			title=post_title,
			text=post_text,
			post_category=category,
			is_published=False
		)
		new_post.save()
		sleep(120)


@shared_task()
def update_news_mailing():
	""" Check new posts in categories, send emails for all mailed user. """

	categories = Category.objects.all()
	users_for_mailing = []

	for category in categories:
		if get_new_posts(category):
			users = User.objects.filter(mailings__id=category.pk)
			if users:
				for user in users:
					if user not in users_for_mailing:
						send_mailing_update_news(user.email)
						users_for_mailing.append(user)
					else:
						continue
