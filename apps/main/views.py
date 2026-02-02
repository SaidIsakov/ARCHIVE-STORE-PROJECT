from django.views.generic import TemplateView, DetailView
from .models import Product, ProductSize
from django.template.response import TemplateResponse
from django.shortcuts import render



class IndexView(TemplateView):
  template_name = 'main/index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["products"] = Product.objects.all()
    return context


  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.headers.get('HX-Request'):
      return TemplateResponse(request, 'main/partials/index.html', context)
    return TemplateResponse(request, self.template_name, context)


class ProductaDetailView(DetailView):
  template_name = 'main/product_detail.html'
  model = Product
  slug_field = 'slug'
  slug_url_kwarg = 'slug'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      return context

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    context = self.get_context_data(**kwargs)
    if request.headers.get('HX-Request'):
      return TemplateResponse(request, 'main/partials/product_detail.html', context)
    return TemplateResponse(request, self.template_name, context)


def search_products(request):
  query = request.GET.get('q')

  if query:
    products = Product.objects.filter(title__icontains=query)
  else:
    products = Product.objects.all()

  context={
    'products': products
    }

  return render(request, 'main/components/products.html', context)
