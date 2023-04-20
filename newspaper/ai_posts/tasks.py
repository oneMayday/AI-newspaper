from django.conf import settings
from django.core.mail import send_mail

from celery import shared_task

from .forms import User
from .models import Category, Post
from .chatgpt_services import chatgpt_get_post
from .services import get_new_posts


@shared_task()
def send_mailing_confirm(user_email, mailing_list):
	"""Sends email when the mailing form has been submitted."""
	send_mail(
			'Подписка оформлена (ALT_stories)',
			f'Вы подписались на категории: {mailing_list}',
			settings.EMAIL_HOST_USER,
			[user_email],
	)


@shared_task()
def send_mailing_update_news(user_email):
	"""Sends email when after creating and publishing new posts."""
	send_mail(
			'ALT_stories',
			f'Для Вас появились новые посты!\nЗайдите на сайт, чтобы посмотреть',
			settings.EMAIL_HOST_USER,
			[user_email],
	)


@shared_task(name='update_news')
def update_news():
	"""Generate new posts with a chatGPT."""
	categories = Category.objects.all()

	for category in categories:
		try:
			post_title, post_text = chatgpt_get_post(category)

			new_post = Post(
				title=post_title,
				text=post_text,
				post_category=category,
				is_published=True
			)
			new_post.save()
		except Exception:
			continue


@shared_task(name='update_news_mailing')
def update_news_mailing():
	"""Check new posts in categories, send emails for all mailed user."""
	categories = Category.objects.all()
	users_for_mailing = []

	for category in categories:
		if get_new_posts(category):
			users = User.objects.filter(mailings__id=category.pk)
			if users:
				try:
					for user in users:
						if user not in users_for_mailing:
							send_mailing_update_news(user.email)
							users_for_mailing.append(user)
						else:
							continue
				except ConnectionError:
					continue
