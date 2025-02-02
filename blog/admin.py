from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created_date', 'approved_comment')
    ordering = ('created_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)