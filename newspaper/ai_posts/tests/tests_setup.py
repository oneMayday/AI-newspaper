from django.test import TestCase
from django.test.client import Client

from ..models import Category, Post, User


class Settings(TestCase):
	def setUp(self):
		super().setUpClass()

		# Create test records in db
		self.category1 = Category.objects.create(
			title='Тестовая категория 1',
			slug='test-category1'
		)

		self.category2 = Category.objects.create(
			title='Тестовая категория 2',
			slug='test-category2'
		)

		self.post1 = Post.objects.create(
			title='Тестовый пост 1',
			text='Текст поста 1',
			post_category=self.category1,
			is_published=True
		)

		self.post2 = Post.objects.create(
			title='Тестовый пост 2',
			text='Текст поста 2',
			post_category=self.category1,
			is_published=False
		)

		self.post3 = Post.objects.create(
			title='Тестовый пост 3',
			text='Текст поста 3',
			post_category=self.category2,
			is_published=True
		)

		self.post4 = Post.objects.create(
			title='Тестовый пост 4',
			text='Текст поста 4',
			post_category=self.category2,
			is_published=False
		)

		# Authorized user
		self.user = User.objects.create_user(
			username='test_user',
			email='test-email@test.ru',
			password='test_password',
		)

		self.user.mailings.set([self.category1, self.category2])

		self.guest_client = Client()
		self.authorized_client = Client()
		self.authorized_client.login(username='test_user', password='test_password')

	def tearDown(self):
		super().tearDown()