from django.contrib import admin
from .models import Category, Subcategory, CategoryAttribute, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title",'pk','category','subcategory','quantity']
    list_filter = ['category','subcategory']























admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(CategoryAttribute)
admin.site.register(Product,ProductAdmin)

