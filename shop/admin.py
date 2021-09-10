from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['category', 'created_by', 'title', 'author', 'price', 'in_stock', 'is_active']
    prepopulated_fields = {'slug', ('title',)}
    list_editable = ['price', 'in_stock']