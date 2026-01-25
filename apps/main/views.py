from django.views.generic import TemplateView, DetailView
from .models import Product, ProductSize

class IndexView(TemplateView):
  template_name = 'main/index.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["products"] = Product.objects.all()
      return context


class ProductaDetailView(DetailView):
  template_name = 'main/product_detail.html'
  model = Product
  slug_field = 'slug'
  slug_url_kwarg = 'slug'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      return context

