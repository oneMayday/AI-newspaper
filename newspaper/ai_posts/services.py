from .forms import User


def get_user_mailing_data(user, mailing_form):
	# Get user email, all user's mailings
	user_email = user.email
	all_user_mailings = User.objects.get(pk=user.pk).mailings.all()

	# Remove old user's mailings from db, add new mailings
	user.mailings.remove(*all_user_mailings)

	for cat in mailing_form.cleaned_data.get('mailing_categories'):
		user.mailings.add(cat)

	# Get new mailings and return it
	new_mailings = User.objects.get(pk=user.pk).mailings.all()
	mailing_text = [elem.title for elem in new_mailings]
	mailing_list = ', '.join(mailing_text)

	return user_email, mailing_list
