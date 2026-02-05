from django.urls import path
from apps.main.views import IndexView, ProductaDetailView, SearchResultsView



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<slug:slug>/', ProductaDetailView.as_view(), name='product-detail'),
    path('searh-products/', SearchResultsView.as_view(), name='search-products')
]
