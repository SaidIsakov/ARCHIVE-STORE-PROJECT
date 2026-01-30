from django.contrib import admin
from apps.main.models import Product, Category, ProductSize, ProductImage, Size, Color, ProductColor


class ProductImageInline(admin.TabularInline):
  model = ProductImage
  extra = 1

class ProductSizeInline(admin.TabularInline):
  model = ProductSize
  extra = 1

class ProductColorInline(admin.TabularInline):
  model = ProductColor
  extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'category', 'price']
  list_filter = ['category']
  search_fields = ['name', 'description']
  prepopulated_fields = {'slug' : ('title',)}
  inlines = [ProductImageInline, ProductSizeInline, ProductColorInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug']
  prepopulated_fields = {'slug' : ('title',)}

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
  list_display = ['title']

@admin.register(Color)
class SizeAdmin(admin.ModelAdmin):
  list_display = ['title', 'hex_code']

