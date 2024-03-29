import openai

from django.conf import settings

from time import sleep


def chatgpt_get_post_header(category):
	"""Create request to chatGPT and recieve post title."""

	completion = openai.Completion.create(
		engine='text-davinci-003',
		prompt=f'Придумай оригинальный заголовок новости о {category.title}. Ограничение - 20 символов.',
		max_tokens=1024,
		temperature=0.5,
		top_p=1
		)

	post_title = completion.choices[0].text.strip('\n')
	return post_title


def chatgpt_get_post_text(category):
	"""Create request to chatGPT and recieve post text."""

	completion = openai.Completion.create(
		engine='text-davinci-003',
		prompt=f'Напиши необычную новость о {category.title} на 2000 символов. Новость должна быть оригинальной и интересной',
		max_tokens=4000,
		temperature=0.5,
		top_p=1,
	)
	post_text = completion.choices[0].text.strip('\n"')
	return post_text


def chatgpt_get_post(category):
	"""Get post content from chatgpt."""

	post_title = chatgpt_get_post_header(category)
	sleep(10)
	post_text = chatgpt_get_post_text(category)
	sleep(20)
	return post_title, post_text
