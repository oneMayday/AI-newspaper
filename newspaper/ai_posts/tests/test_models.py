from django.test import TestCase

from ..models import Category, Post, User


class Settings(TestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()

		# Create test records in db
		cls.category1 = Category.objects.create(
			title='Тестовая категория 1',
			slug='test-category1'
		)

		cls.category2 = Category.objects.create(
			title='Тестовая категория 2',
			slug='test-category2'
		)

		cls.post1 = Post.objects.create(
			title='Тестовый пост 1',
			text='Текст поста 1',
			post_category=cls.category1,
			is_published=True
		)

		cls.post2 = Post.objects.create(
			title='Тестовый пост 2',
			text='Текст поста 2',
			post_category=cls.category1,
			is_published=False
		)

		cls.post3 = Post.objects.create(
			title='Тестовый пост 3',
			text='Текст поста 3',
			post_category=cls.category2,
			is_published=True
		)

		cls.post4 = Post.objects.create(
			title='Тестовый пост 4',
			text='Текст поста 4',
			post_category=cls.category2,
			is_published=False
		)

		cls.user = User.objects.create_user(
			username='test_user',
			email='test-email@test.ru',
			password='test_password',
		)

		cls.user.mailings.set([cls.category1, cls.category2])

	@classmethod
	def tearDownClass(cls):
		super().tearDownClass()


class CategoryTest(Settings):
	def test_tags(self):
		self.assertEqual(self.category1.title, 'Тестовая категория 1')
		self.assertEqual(self.category1.slug, 'test-category1')


class PostTest(Settings):
	def test_tags(self):
		self.assertEqual(self.post1.title, 'Тестовый пост 1')
		self.assertEqual(self.post1.text, 'Текст поста 1')
		self.assertEqual(self.post1.post_category, self.category1)
		self.assertEqual(self.post1.is_published, True)

	def test_published_posts(self):
		self.assertEqual([post for post in Post.objects.filter(is_published=True)], [self.post1, self.post3])

	def test_unpublished_posts(self):
		self.assertEqual([post for post in Post.objects.filter(is_published=False)], [self.post2, self.post4])


class UserTest(Settings):
	def test_tags(self):
		self.assertEqual(self.user.username, 'test_user')
		self.assertEqual(self.user.email, 'test-email@test.ru')
		self.assertEqual([category for category in self.user.mailings.all()], [self.category1, self.category2])

	def test_del_mailing(self):
		self.user.mailings.remove(self.category1)
		self.assertEqual([category for category in self.user.mailings.all()], [self.category2])
