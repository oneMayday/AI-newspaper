from django.http import Http404

from .tests_setup import Settings
from ..services import get_post, get_all_posts_from_category


class ServicesTest(Settings):
	def test_get_post(self):
		# try to get published posts
		category, target_post = get_post(self.category1.slug, 1)
		self.assertEqual((category, target_post), (self.category1, self.post1))

		# try to get unpublished post
		self.assertRaises(Http404, get_post, self.category1.slug, 2)

	# def test_all_posts_from_category(self):
	# 	request = self.request_factory.get(f'categories/{self.category1.slug}/')
	# 	category, page_obj = get_all_posts_from_category(request, self.category1.slug)
	# 	print(request, category, page_obj.object_list, '!!!!!!!!')