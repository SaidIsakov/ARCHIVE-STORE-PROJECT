from django.db import models
from django.utils.text import slugify

class Category(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField(unique=True)

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)

  def __str__(self):
    return self.title

class Color(models.Model):
  title = models.CharField(max_length=55)
  hex_code = models.CharField(max_length=7, blank=True, help_text="Например, #FF0000")

  def __str__(self):
    return self.title

class ProductColor(models.Model):
  product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_color')
  color = models.ForeignKey(Color, on_delete=models.CASCADE)




class Size(models.Model):
  title = models.CharField(max_length=20)

  def __str__(self):
    return self.title

class ProductSize(models.Model):
  product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_size')
  size = models.ForeignKey(Size, on_delete=models.CASCADE)
  stock = models.PositiveIntegerField(default=0)

  def __str__(self):
    return f"{self.size.title} ({self.stock} in stock for {self.product.title})"

class Product(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField(max_length=200, blank=True)
  brand_name = models.CharField(max_length=20)
  main_image = models.ImageField(upload_to='products/main/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)

  def __str__(self):
    return self.title


class ProductImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
  image = models.ImageField(upload_to='products/extra/')
