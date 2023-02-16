from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import *


User = get_user_model()


class UserCreateForm(UserCreationForm):
	""" Кастомная форма авторизации с полем email """
	email = forms.EmailField(
		label='Email',
		max_length=254,
		widget=forms.EmailInput(attrs={'autocomplete': 'email'})
	)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email')


# Формируем список кортежей в формате ("заголовок категории", "заголовок категории"),
# для заполнения формы чекбокса (класс Mailings)
CATEGORIES = [(category.title, category.title) for category in Category.objects.all()]


class Mailing(forms.Form):
	""" Форма подписки на рассылку"""
	name = forms.CharField(label='Введите имя', max_length=120)
	email = forms.EmailField(label='Введите email')
	mailing_categories = forms.MultipleChoiceField(
		label='Выберите категории',
		choices=CATEGORIES,
		widget=forms.CheckboxSelectMultiple(),
	)
