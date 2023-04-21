from django import template

from ..models import Category


register = template.Library()


@register.simple_tag()
def get_categories():
	try:
		categories = Category.objects.all()
	except Exception:
		categories = 'Тут пока пусто, заполните значения через админку'
	return categories
