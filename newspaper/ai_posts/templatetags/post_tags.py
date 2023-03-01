from django import template

from ..models import Post


register = template.Library()


@register.simple_tag(name='last-post')
def get_last_post(filt=None):
	try:
		return Post.objects.filter(post_category_id=filt, is_published=True).order_by('-time_create')[0]
	except IndexError:
		return 'Упс... Для данной категории пока нет новостей'

#
# @register.simple_tag(name='all-posts')
# def get_all_posts(cat_id=None):
# 	posts = Post.objects.filter(post_category_id=cat_id, is_published=True).order_by('-time_create')
# 	if posts:
# 		return posts
