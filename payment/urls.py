from django.urls import path

from . import views
from .apps import PaymentConfig

app_name = PaymentConfig.name

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
]
