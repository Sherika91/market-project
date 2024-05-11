from django.urls import path

from . import views
from .apps import OrdersConfig

app_name = OrdersConfig.name

urlpatters = [
    path('create/', views.order_create, name='order_create')
]
