from django import forms

from .models import *


# Формируем список кортежей в формате ("заголовок категории", "заголовок категории"), для заполнения формы чекбокса
CATEGORIES = [(category.title, category.title) for category in Category.objects.all()]


class Mailing(forms.Form):
	name = forms.CharField(label='Введите имя', max_length=120)
	email = forms.EmailField(label='Введите email')
	mailing_categories = forms.MultipleChoiceField(
		label='Выберите категории',
		choices=CATEGORIES,
		widget=forms.CheckboxSelectMultiple()
	)
