from django.contrib import admin

# v1 book
from .models import Post

# net
from django.db import models

#@admin.register(Post)
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')


