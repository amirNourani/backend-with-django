from django.contrib import admin
from .models import Food, Category
# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_suggested', 'category']
    list_filter = ['category']
    list_editable = ['price', 'category', 'is_suggested']
    search_fields = ['name']
    ordering = ['category', 'name']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    