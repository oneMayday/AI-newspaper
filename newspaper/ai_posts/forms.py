from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import *


User = get_user_model()


class UserCreateForm(UserCreationForm):
	""" Кастомная форма авторизации с полем email """
	email = forms.EmailField(
		label='Email',
		max_length=254,
		widget=forms.EmailInput(attrs={'autocomplete': 'email'})
	)

	error_messages = {
		"password_mismatch": _("The two password fields didn’t match."),
		"email_exist": _("Пользователь с таким почтовым адресом уже существует"),
	}

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email')

	def clean_email(self):
		# Обработка уникальности email
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).exists():
			raise forms.ValidationError(
				self.error_messages["email_exist"],
				code="email_exist",
			)

		return email


# Формируем список кортежей в формате ("заголовок категории", "заголовок категории"),
# для заполнения формы чекбокса (класс Mailings)
CATEGORIES = [(category.title, category.title) for category in Category.objects.all()]


class Mailing(forms.Form):
	""" Форма подписки на рассылку"""

	mailing_categories = forms.MultipleChoiceField(
		label='Выберите категории',
		choices=CATEGORIES,
		widget=forms.CheckboxSelectMultiple(),
	)
