from datetime import date

from ..models import Post
from ..templatetags.category_tags import get_categories
from ..templatetags.post_tags import get_last_post
from .tests_setup import Settings


class CategoryTest(Settings):
	def test_get_categories(self):
		self.assertEqual([*get_categories()], [self.category1, self.category2])


class PostTest(Settings):
	def test_get_last_post_positive(self):
		last_post = get_last_post(self.category1.pk)
		self.assertEqual(last_post, self.post1)

		self.new_post = Post(
			title='Last post',
			text='Actually last post',
			post_category=self.category1,
			is_published=True
		)
		self.new_post.save()
		self.new_post.time_create = date(2025, 12, 5)
		self.new_post.save()

		last_post = get_last_post(self.category1.pk)
		self.assertEqual(last_post, self.new_post)

	def test_get_last_post_negative(self):
		self.new_post = Post(
			title='Last post',
			text='Actually last post',
			post_category=self.category1,
			is_published=False
		)
		self.post1.is_published = False
		self.post1.save()

		last_post = get_last_post(self.category1.pk)
		self.assertEqual(last_post, 'Упс... Для данной категории пока нет новостей')
