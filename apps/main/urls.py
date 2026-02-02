from django.urls import path
from apps.main.views import IndexView, ProductaDetailView, search_products



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<slug:slug>/', ProductaDetailView.as_view(), name='product-detail'),
    path('searh-products/', search_products, name='search-products')
]
