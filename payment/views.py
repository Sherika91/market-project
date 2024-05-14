import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, reverse, redirect

from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, order_id)
    if request.method == 'POSt':
        succes_url = request.build_absolute_uri(
            reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(
            reverse('payment:canceled'))

        # Stripe checkout session data
        session_data = {
            'mode': 'payment',
            'client_reference_id': order_id,
            'success_url': succes_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)

        # redirect to a Stripe payment form
        return redirect(session.url, code=303)
    else:
        return redirect(request, 'payment/process.html', locals())
