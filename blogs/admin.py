from re import search
from django.contrib import admin
from .models import Blog, Category, Tag, Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('active', 'time')
    list_editable = ('active', )
    list_display = ('email', 'comment', 'time', 'active')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'category')
    list_filter = ('author', 'category', 'tags', 'created_at')
    search_fields = ('title',)
    ordering = ('author', 'created_at', 'title', 'category')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title', )}
    
        
@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title', )}
    
    