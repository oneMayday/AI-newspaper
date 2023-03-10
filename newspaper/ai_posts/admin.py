from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'post_category', 'time_create', 'is_published',)
	list_display_links = ('title',)
	list_editable = ('is_published',)
	list_filter = ('time_create', 'is_published',)
	search_fields = ('title',)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(User)


