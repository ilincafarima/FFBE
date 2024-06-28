from django.contrib import admin
from .models import BlogPost, Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timestamp', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('author', 'timestamp')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'timestamp', 'updated')
    search_fields = ('body',)
    list_filter = ('author', 'timestamp')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
