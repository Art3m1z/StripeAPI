import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views import View

from api_stripe.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class CancelView(TemplateView):
    template_name = "api_stripe/cancel.html"


class SuccessesView(TemplateView):
    template_name = "api_stripe/successes.html"


class ProductLandingPageView(TemplateView):
    template_name = "api_stripe/landing.html"

    def get_context_data(self, pk, **kwargs):
        product = Item.objects.get(id=pk)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY,
            "product": product
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        product = Item.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {

                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class DisplayItemsView(View):

    def get(self, request):
        product = Item.objects.all()
        template = 'api_stripe/lst_items.html'

        return render(request, template, {'product': product})
