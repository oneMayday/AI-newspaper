from django import template

from ..models import Post

register = template.Library()


@register.simple_tag()
def get_all_posts(filter=None):
	return Post.objects.filter(pk=filter)
