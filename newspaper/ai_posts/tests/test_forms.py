from .tests_setup import Settings
from ..forms import Mailing, UserCreateForm


class FormsTest(Settings):
	def test_mailing_form_negative(self):
		form_data = {}
		self.mailing_form = Mailing(data=form_data)

		self.assertFalse(self.mailing_form.is_valid())

	def test_mailing_form_positive(self):
		form_data = {'mailing_categories': (3, 5)}
		self.mailing_form = Mailing(data=form_data)

		self.assertTrue(self.mailing_form.is_valid())

	def test_user_creation_form_empty_poles_negative(self):
		form_data = {}
		self.mailing_form = UserCreateForm(data=form_data)

		self.assertFalse(self.mailing_form.is_valid())

	def test_user_creation_form_user_already_exists_negative(self):
		form_data = {
			'username': 'test_user_10',
			'email': 'test-email@test.ru',
			'password1': 'username10_password',
			'password2': 'username10_password',
		}
		self.mailing_form = UserCreateForm(data=form_data)

		expected_error = 'Пользователь с таким почтовым адресом уже существует.'
		expected_result = expected_error in self.mailing_form.errors['email']

		self.assertTrue(expected_result)

	def test_user_creation_form_password_mismatch_negative(self):
		form_data = {
			'username': 'test_user_10',
			'email': 'test_username@testmail.com',
			'password1': 'username10_password_111',
			'password2': 'username10_password',
		}
		self.mailing_form = UserCreateForm(data=form_data)

		expected_error = 'Введенные пароли не совпадают.'
		expected_result = expected_error in self.mailing_form.errors['password2']

		self.assertTrue(expected_result)

	def test_user_creation_form_valid_data_positive(self):
		form_data = {
			'username': 'test_username',
			'email': 'test_username@testmail.com',
			'password1': 'username10_password',
			'password2': 'username10_password',
		}
		self.mailing_form = UserCreateForm(data=form_data)

		self.assertTrue(self.mailing_form.is_valid())
