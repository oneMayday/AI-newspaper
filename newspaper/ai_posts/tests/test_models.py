from .tests_setup import Settings
from ..models import Post


class CategoryTest(Settings):
	def test_tags(self):
		self.assertEqual(self.category1.title, 'Тестовая категория 1')
		self.assertEqual(self.category1.slug, 'test-category1')
		self.assertEqual(self.category1._meta.verbose_name, 'Категория')
		self.assertEqual(self.category1._meta.verbose_name_plural, 'Категории')

	def test_meta_poles(self) -> None:
		self.assertEqual(self.category1._meta.verbose_name, 'Категория')
		self.assertEqual(self.category1._meta.verbose_name_plural, 'Категории')


class PostTest(Settings):
	def test_tags(self):
		self.assertEqual(self.post1.title, 'Тестовый пост 1')
		self.assertEqual(self.post1.text, 'Текст поста 1')
		self.assertEqual(self.post1.post_category, self.category1)
		self.assertEqual(self.post1.is_published, True)
		self.assertEqual(self.post1._meta.verbose_name, 'Пост')
		self.assertEqual(self.post1._meta.verbose_name_plural, 'Посты')

	def test_published_posts(self):
		self.assertEqual([post for post in Post.objects.filter(is_published=True)], [self.post1, self.post3])

	def test_unpublished_posts(self):
		self.assertEqual([post for post in Post.objects.filter(is_published=False)], [self.post2, self.post4])

	def test_meta_poles(self) -> None:
		self.assertEqual(self.category1._meta.verbose_name, 'Пост')
		self.assertEqual(self.category1._meta.verbose_name_plural, 'Посты')


class UserTest(Settings):
	def test_tags(self):
		self.assertEqual(self.user.username, 'test_user')
		self.assertEqual(self.user.email, 'test-email@test.ru')
		self.assertEqual([category for category in self.user.mailings.all()], [self.category1, self.category2])

	def test_del_mailing(self):
		self.user.mailings.remove(self.category1)
		self.assertEqual([category for category in self.user.mailings.all()], [self.category2])
