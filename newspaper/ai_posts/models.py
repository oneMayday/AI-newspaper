from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    """News categories model."""
    title = models.CharField(max_length=30, verbose_name='Категория')
    slug = models.SlugField(max_length=30, unique=True, null=True, verbose_name="Slug")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']


class Post(models.Model):
    """Newspaper posts model."""
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    text = models.TextField(max_length=1600, verbose_name='Текст статьи')
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    post_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['time_create', 'title']


class User(AbstractUser):
    """Custom user model with an additional field - 'mailings' - mailing list."""
    mailings = models.ManyToManyField(Category)
