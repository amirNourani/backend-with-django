from django.contrib import admin
from .models import Food
# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('food_type',)
    list_editable = ('description', 'price')
    search_fields = ('name',)