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
			error_adress = f'Ошибка доступа к странице {page}'
			error_template = f'	Ошибка: {page} ожидал шаблон {template}'
			self.assertEqual(response.status_code, 200, error_adress)
			self.assertTemplateUsed(response, template, error_template)

	def test_register_page(self):
		"""Tests for auth and non-auth users."""
		# Auth users
		response = self.authorized_client.get('/register/')
		self.assertRedirects(response, '/')

		# Non-auth users
		response = self.guest_client.get('/register/')
		error_adress = f'Ошибка доступа к странице /register/'
		error_template = f'	Ошибка: /register/ ожидал шаблон ai_posts/registration/register.html'
		self.assertEqual(response.status_code, 200, error_adress)
		self.assertTemplateUsed(response, 'registration/register.html', error_template)

	def test_profile_page(self):
		"""Tests for auth and non-auth users."""
		# Auth users
		response = self.authorized_client.get(f'/profile/{self.user.pk}/')
		error_adress = f'Ошибка доступа к странице /profile/{self.user.pk}/'
		error_template = f'	Ошибка: /profile/{self.user.pk}/ ожидал шаблон ai_posts/profile.html'
		self.assertEqual(response.status_code, 200, error_adress)
		self.assertTemplateUsed(response, 'ai_posts/profile.html', error_template)

		# Non-auth users
		response = self.guest_client.get(f'/profile/{self.user.pk}/')
		self.assertRedirects(response, '/register/')

	def test_mailing_page_guest_user(self):
		"""Tests for auth and non-auth users."""
		# Auth users
		response = self.authorized_client.get(f'/mailing/')
		error_adress = f'Ошибка доступа к странице /mailing/'
		error_template = f'	Ошибка: /mailing/ ожидал шаблон ai_posts/mailing.html'
		self.assertEqual(response.status_code, 200, error_adress)
		self.assertTemplateUsed(response, 'ai_posts/mailing.html', error_template)

		# Non-auth users
		response = self.guest_client.get(f'/mailing/')
		self.assertRedirects(response, '/register/')
