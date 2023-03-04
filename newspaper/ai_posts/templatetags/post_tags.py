from django import template

from ..models import Post


register = template.Library()


@register.simple_tag(name='last-post')
def get_last_post(filt=None):
	try:
		return Post.objects.filter(post_category_id=filt, is_published=True).order_by('-time_create')[0]
	except IndexError:
		return 'Упс... Для данной категории пока нет новостей'
