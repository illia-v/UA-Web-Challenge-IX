from django.shortcuts import render
from django.views.generic import DetailView

from .models import Order


def index(request):
    """
    A main page view of Our Pizzeria.
    """
    return render(request, 'our_pizzeria/index.html')


class OrderDetailView(DetailView):
    """
    A view of an order page.
    """
    template_name = 'our_pizzeria/order.html'
    context_object_name = 'order'
    queryset = Order.objects.all()
