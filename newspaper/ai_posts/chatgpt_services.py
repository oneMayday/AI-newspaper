import openai

from django.conf import settings


def chatgpt_get_post_header(category):
	""" Create request to chatGPT and recieve post header """

	completion = openai.Completion.create(
		engine='text-davinci-003',
		prompt=f'Придумай заголовок новости о {category.title}. Ограничение - 20 символов.',
		max_tokens=1024,
		temperature=0.5,
		top_p=1
		)

	post_title = completion.choices[0].text
	return post_title


def chatgpt_get_post_text(category):
	""" Create request to chatGPT and recieve post text """

	completion = openai.Completion.create(
		engine='text-davinci-003',
		prompt=f'Напиши выдуманную статью о {category.title} на 1500 символов',
		max_tokens=4000,
		temperature=0.5,
		top_p=1,
	)
	post_text = completion.choices[0].text
	return post_text


def chatgpt_get_post(category):
	""" Get post content from chatgpt """

	post_title = chatgpt_get_post_header(category)
	post_text = chatgpt_get_post_text(category)
	return post_title, post_text
