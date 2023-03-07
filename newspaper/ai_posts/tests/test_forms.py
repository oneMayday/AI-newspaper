from django import forms

from .tests_setup import Settings
from ..forms import Mailing


class FormsTest(Settings):
	def test_mailing_form(self):
		form_data = {}
		self.mailing_form = Mailing(data=form_data)
		self.assertFalse(self.mailing_form.is_valid())

		# form_data = {self.category1.pk: self.category1}
		self.mailing_form = Mailing(data={1: 1})

		self.assertTrue(self.mailing_form.is_valid(), 'Ошибка')