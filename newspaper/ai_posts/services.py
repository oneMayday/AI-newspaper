from datetime import date

from .forms import User
from .models import Post


def get_user_mailing_data(user, mailing_form):
	""" Remove old user's mailings from db, add new mailings. """

	user_email = user.email
	clear_user_mailings(user)

	for cat in mailing_form.cleaned_data.get('mailing_categories'):
		user.mailings.add(cat)

	# Get new mailings and return it
	new_mailings = User.objects.get(pk=user.pk).mailings.all()
	mailing_text = [elem.title for elem in new_mailings]
	mailing_list = ', '.join(mailing_text)

	return user_email, mailing_list


def clear_user_mailings(user):
	""" Get all user's mailings and cleat it. """

	all_user_mailings = User.objects.get(pk=user.pk).mailings.all()
	user.mailings.remove(*all_user_mailings)


def get_new_posts(category):
	""" Get new published posts for today. """

	today_date = date.today()
	today_posts = Post.objects.filter(time_create=today_date, post_category=category.pk, is_published=True)
	return True if today_posts else False
