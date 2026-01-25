from django.contrib import admin
from apps.main.models import Product, Category, ProductSize, ProductImage, Size


class ProductImageInline(admin.TabularInline):
  model = ProductImage
  extra = 1

class ProductSizeInline(admin.TabularInline):
  model = ProductSize
  extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'category', 'color', 'price']
  list_filter = ['color', 'category']
  search_fields = ['name', 'color', 'description']
  prepopulated_fields = {'slug' : ('title',)}
  inlines = [ProductImageInline, ProductSizeInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug']
  prepopulated_fields = {'slug' : ('title',)}

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
  list_display = ['title']



