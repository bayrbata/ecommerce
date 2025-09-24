from django.contrib import admin
from .models import Category, Product

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Product, ProductAdmin)