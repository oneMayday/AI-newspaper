from django.test import TestCase
from django.test.utils import override_settings

from .. import tasks


class AddTestCase(TestCase):
	@override_settings(
		CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
		CELERY_ALWAYS_EAGER=True,
		BROKER_BACKEND='memory'
	)
	def test_send_mailing_cofirm(self):
		task = tasks.send_mailing_confirm\
			.s(user_email='test_email@gmail.com', mailing_list=['Spodasdsart'])\
			.apply()

		self.assertEqual(task.status, 'SUCCESS')

	@override_settings(
		CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
		CELERY_ALWAYS_EAGER=True,
		BROKER_BACKEND='memory'
	)
	def test_send_mailing_update_news(self):
		task = tasks.send_mailing_update_news.s(user_email='test_email@gmail.com').apply()

		self.assertEqual(task.status, 'SUCCESS')

	@override_settings(
		CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
		CELERY_ALWAYS_EAGER=True,
		BROKER_BACKEND='memory'
	)
	def test_send_update_news(self):
		task = tasks.update_news.s().apply()

		self.assertEqual(task.status, 'SUCCESS')

	@override_settings(
		CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
		CELERY_ALWAYS_EAGER=True,
		BROKER_BACKEND='memory'
	)
	def test_update_news_mailing(self):
		task = tasks.update_news_mailing.s().apply()

		self.assertEqual(task.status, 'SUCCESS')
