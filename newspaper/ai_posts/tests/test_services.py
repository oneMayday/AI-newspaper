from django.http import Http404

from .tests_setup import Settings
from ..models import User, Category
from ..services import get_post, get_all_posts_from_category, clear_user_mailings, get_new_posts, get_user_mailing_data


class ServicesTest(Settings):
	def test_get_post(self):
		"""Get published post from category."""
		# try to get published post
		category, target_post = get_post(self.category1.slug, 1)
		self.assertEqual((category, target_post), (self.category1, self.post1))

		# try to get unpublished post
		self.assertRaises(Http404, get_post, self.category1.slug, 2)

	def test_get_all_posts_from_category(self):
		"""Get all published posts from category."""
		request = self.request_factory.get(f'categories/{self.category1.slug}/')
		category, page_obj = get_all_posts_from_category(request, self.category1.slug)
		self.assertEqual(*page_obj.object_list, self.post1)

	def test_clear_user_mailings(self):
		"""Create new user and clear his mailings"""
		new_user = User.objects.create_user(
			username='new_user',
			email='new_user@test.com',
			password='new_user_password'
		)
		new_user.mailings.set([self.category1, self.category2])
		clear_user_mailings(new_user)
		user_mailings = [*new_user.mailings.all()]
		self.assertEqual(user_mailings, [])

	def test_get_new_posts(self):
		new_category = Category.objects.create(
			title='new_category',
			slug='new-cat-slug'
		)
		today_posts = get_new_posts(self.category1)
		self.assertTrue(today_posts)
		today_posts = get_new_posts(new_category)
		self.assertFalse(today_posts)
