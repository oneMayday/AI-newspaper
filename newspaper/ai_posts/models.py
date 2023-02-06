from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=1600)
    time_create = models.DateField(auto_now_add=True)
    post_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
