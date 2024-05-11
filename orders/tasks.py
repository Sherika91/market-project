from celery import shared_task
from django.core.mail import send_mail

from myshop import settings
from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order_id}"
    message = (f"Dear {order.first_name}, \n\n "
               f"You have succesfully placed and order."
               f"Your order ID is {order_id}.")
    mail_sent = send_mail(subject=subject,
                          message=message,
                          from_email=settings.EMAIL_HOST_USER,
                          recipient_list=[order.email],
                          fail_silently=False)
    return mail_sent
