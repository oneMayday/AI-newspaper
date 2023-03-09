import datetime

from .tests_setup import Settings
from ..models import Post
from ..templatetags.category_tags import get_categories
from ..templatetags.post_tags import get_last_post


class CategoryTest(Settings):
	def test_get_categories(self):
		self.assertEqual([*get_categories()], [self.category1, self.category2])


class PostTest(Settings):
	def test_get_last_post(self):
		last_post = get_last_post(self.category1.pk)
		self.assertEqual(last_post, self.post1)

		new_post = Post(
			title='Last post',
			text='Actually last post',
			post_category=self.category1,
			is_published=True
		)
		new_post.save()
		new_post.time_create = datetime.date(2025, 12, 5)
		new_post.save()

		last_post = get_last_post(self.category1.pk)
		self.assertEqual(last_post, new_post)
