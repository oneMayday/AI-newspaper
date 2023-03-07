from django.urls import reverse

from .tests_setup import Settings


class ViewsTest(Settings):
	def test_home_correct_context_and_template(self):
		page = reverse('home')
		context = {'title': 'Главная', }
		template = 'ai_posts/index.html'

		response = self.guest_client.get(page)
		self.assertEqual(response.context['title'], context['title'])
		self.assertTemplateUsed(response, template)

	def test_register_correct_context_and_template(self):
		page = reverse('register')
		context = {'title': 'Регистрация', }
		template = 'registration/register.html'

		# Allowed only for guest users.
		response = self.guest_client.get(page)
		self.assertEqual(response.context['title'], context['title'])
		self.assertTemplateUsed(response, template)

	def test_about_correct_context_and_template(self):
		page = reverse('about')
		context = {'title': 'О нас/Контакты', }
		template = 'ai_posts/about.html'

		response = self.guest_client.get(page)
		self.assertEqual(response.context['title'], context['title'])
		self.assertTemplateUsed(response, template)

	def test_profile_correct_context_and_template(self):
		page = reverse('profile', kwargs={'user_id': self.user.pk})
		context = {'title': 'Личный кабинет', }
		template = 'ai_posts/profile.html'

		# Allowed only for authenticated users.
		response = self.authorized_client.get(page)
		self.assertEqual(response.context['title'], context['title'])
		self.assertTemplateUsed(response, template)

	def test_clear_mailings_correct_context_and_template(self):
		page = reverse('clear_mailings', kwargs={'user_id': self.user.pk})

		# For guest users.
		response = self.guest_client.get(page)
		self.assertRedirects(response, reverse('register'))

		# For authenticated users.
		response = self.authorized_client.get(page)
		self.assertRedirects(response, reverse('profile', kwargs={'user_id': self.user.pk}))

	def test_categories_correct_context_and_template(self):
		page = reverse('categories')
		context = {'title': 'Категории', }
		template = 'ai_posts/categories.html'

		response = self.guest_client.get(page)
		self.assertEqual(response.context['title'], context['title'])
		self.assertTemplateUsed(response, template)

	def test_all_posts_correct_context_and_template(self):
		page = reverse('all_posts', kwargs={'cat_slug': self.category1.slug})
		context = {
			'title': self.category1.title,
			'category': self.category1,
			'expected_posts': '.Тестовый пост 1',
		}
		template = 'ai_posts/all_posts.html'

		response = self.guest_client.get(page)
		self.assertEqual(response.context['title'], context['title'])
		self.assertEqual(response.context['category'], context['category'])
		self.assertEqual(*response.context['page_obj'], self.post1)
		self.assertTemplateUsed(response, template)