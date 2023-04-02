from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from datetime import date

from .forms import User
from .models import Post, Category


def get_all_posts_from_category(request, cat_slug):
	"""Get all posts from category (paginated)."""
	category = get_object_or_404(Category, slug=cat_slug)
	posts = Post.objects.filter(post_category_id=category.id, is_published=True).order_by('-time_create')
	page_obj = pagination(request, posts)
	return category, page_obj


def pagination(request, posts):
	"""Pagintaion posts list"""
	posts_paginator = Paginator(posts, 5)
	page_number = request.GET.get('page')
	page_obj = posts_paginator.get_page(page_number)
	return page_obj


def get_post(cat_slug, post_id):
	"""Get post"""
	category = get_object_or_404(Category, slug=cat_slug)
	target_post = get_object_or_404(Post, pk=post_id, is_published=True)
	return category, target_post


def get_user_mailing_data(user=None, mailing_form=None):
	"""Remove old user's mailings from db, add new mailings or return user mailing list."""
	if mailing_form:
		clear_user_mailings(user)

		for cat in mailing_form.cleaned_data.get('mailing_categories'):
			user.mailings.add(cat)

	# Get new mailings and return it.
	new_mailings = User.objects.get(pk=user.pk).mailings.all()
	mailing_text = [elem.title for elem in new_mailings]
	mailing_list = ', '.join(mailing_text)
	return mailing_list


def clear_user_mailings(user):
	"""Get all user's mailings and clear it."""
	all_user_mailings = User.objects.get(pk=user.pk).mailings.all()
	user.mailings.remove(*all_user_mailings)


def get_new_posts(category):
	"""Get new published posts for today."""
	today_date = date.today()
	today_posts = Post.objects.filter(time_create=today_date, post_category=category.pk, is_published=True)
	return True if today_posts else False
