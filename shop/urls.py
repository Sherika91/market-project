from django.urls import path

from . import views
from .apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:categoy_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
