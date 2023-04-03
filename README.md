<h3>Описание:</h3>
Проект новостного сайта, контент для которого автоматически генерируются нейросетью Chat GPT-3.\
Обновление происходит 1 раз в сутки, реализована регистрация пользоваталей, подписка на рассылку, на интересующие темы.
При обновлении новостной базы происходит рассылка пользователям, подписанным на соответствующие категории.


[url=https://postimg.cc/YLzHDkgg][img]https://i.postimg.cc/YLzHDkgg/cats.png[/img][/url]

[url=https://postimg.cc/QHSDp8jZ][img]https://i.postimg.cc/QHSDp8jZ/main.jpg[/img][/url]

[url=https://postimg.cc/3d06w3WZ][img]https://i.postimg.cc/3d06w3WZ/posts.png[/img][/url]

[url=https://postimg.cc/rD6H07r2][img]https://i.postimg.cc/rD6H07r2/reg.png[/img][/url]


<h3>Порядок установки:</h3>
<details>
<summary>Установка виртуального окружения и зависимостей</summary>
<br>

1) Клонируем репозиторий:
	

	https://github.com/oneMayday/AI-newspaper.git
2) Создаем виртуальное окружение и активируем его: 


	python -m venv venv

	Windows: venv\Scripts\activate.bat
	Linux и MacOS: source venv/bin/activate

3) Переходим в директорию проекта и устанавливаем зависимости:


	pip install -r requirements.txt
4) Переходим в директорию newspaper.\
Файл example.env переименовываем в .env, прописываем в нём свои ключи и данные SMTP сервера.
5) Выполняет миграции:


	python manage.py migrate
6) Запускаем сервер:
	

	python manage.py runserver

</details>


<details>
<summary>Установка и настройка Redis, Celery и Celery-beat.</summary>
<br>
Для работы отложенных задач и задач по расписанию необходимо запустить 3 отдельных сервера,
именно в том порядке, какой указан в инструкции (redis, celery-beat, celery):

Redis:\
Перейти в папку с установленным Redis и последовательно ввести в консоли:

	.\redis-server start
	.\redis-cli
В консоли должен появиться адрес (по умолчанию 127.0.0.1:6379). 
Проверить работу можно командой PING -> сервер должен ответить PONG.

Celery-beat:\
Перейти в папку с проектом (туда, где находится manage.py) и ввести в консоль:

	celery --app newspaper beat -l info

Celery:\
Перейти в папку с проектом (туда, где находится manage.py) и ввести в консоль:

	celery -A newspaper worker --loglevel=info

ВАЖНО! Для использования под Windows нужно импользовать другую команду:

	celery --app=newspaper worker --pool=solo --loglevel=info

По умолчанию статьи добавляются в базу данных неопубликованными.\
Добаление в основную ленту осуществляется установкой флага is_published = True в бд или через админку.
Если хочется изменить это поведение (чтобы статьи сразу добавлялись как опубликованные), нужно в ai_posts/tasks изменить значение в функции:

	@shared_task(name='update_news')
	def update_news():
		...
		new_post = Post(...
			is_published=True
		)
		...
</details>