from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import *


User = get_user_model()


class UserCreateForm(UserCreationForm):
	""" Custom authorization form with email field.
	"""

	email = forms.EmailField(
		label='Email',
		max_length=254,
		widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
	)

	error_messages = {
		"password_mismatch": _("The two password fields didn’t match."),
		"email_exist": _("Пользователь с таким почтовым адресом уже существует"),
	}

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email')

	def clean_email(self):
		# Uniqueness processing mail.
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).exists():
			raise forms.ValidationError(
				self.error_messages["email_exist"],
				code="email_exist",
			)

		return email


# Forming list of tuples in format("category pk", "category title") for completion checkbox form.
CATEGORIES = [(category.pk, category) for category in Category.objects.all()]


class Mailing(forms.Form):
	""" Mailing form.
	"""

	mailing_categories = forms.MultipleChoiceField(
		label='Выберите категории',
		choices=CATEGORIES,
		widget=forms.CheckboxSelectMultiple(),
	)
