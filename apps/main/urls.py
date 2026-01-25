from django.urls import path
from apps.main.views import IndexView, ProductaDetailView



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<slug:slug>/', ProductaDetailView.as_view(), name='product-detail')
]
