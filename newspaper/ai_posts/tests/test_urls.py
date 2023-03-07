from .tests_setup import Settings


class UrlsTest(Settings):
	def test_pages_for_all_users(self):
		"""Tests pages, same for auth and not auth users."""
		pages = {
			'/': 'ai_posts/index.html',
			'/about/': 'ai_posts/about.html',
			'/categories/': 'ai_posts/categories.html',
			f'/categories/{self.category1.slug}/': 'ai_posts/all_posts.html',
			f'/categories/{self.category1.slug}/{self.post1.id}/': 'ai_posts/post.html',
		}

		for page, template in pages.items():
			response = self.guest_client.get(page)
			self.assertEqual(response.status_code, 200, self.url_page_error(page))
			self.assertTemplateUsed(response, template, self.url_template_error(page, template))

	def test_register_page(self):
		"""Tests for auth and non-auth users."""
		page = '/register/'
		template = 'registration/register.html'

		# Auth users
		response = self.authorized_client.get(page)
		self.assertRedirects(response, '/')

		# Non-auth users
		response = self.guest_client.get(page)
		self.assertEqual(response.status_code, 200, self.url_page_error(page))
		self.assertTemplateUsed(response, template, self.url_template_error(page, template))

	def test_profile_page(self):
		"""Tests for auth and non-auth users."""
		page = f'/profile/{self.user.pk}/'
		template = 'ai_posts/profile.html'

		# Auth users
		response = self.authorized_client.get(page)
		self.assertEqual(response.status_code, 200, self.url_page_error(page))
		self.assertTemplateUsed(response, template, self.url_template_error(page, template))

		# Non-auth users
		response = self.guest_client.get(page)
		self.assertRedirects(response, '/register/')

	def test_mailing_page_guest_user(self):
		"""Tests for auth and non-auth users."""
		page = '/mailing/'
		template = 'ai_posts/mailing.html'

		# Auth users
		response = self.authorized_client.get(page)
		self.assertEqual(response.status_code, 200, self.url_page_error(page))
		self.assertTemplateUsed(response, template, self.url_template_error(page, template))

		# Non-auth users
		response = self.guest_client.get(page)
		self.assertRedirects(response, '/register/')
