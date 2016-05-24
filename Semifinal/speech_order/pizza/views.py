from datetime import datetime
from re import split as re_split

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, View

from .models import PizzaOrder
from .send_order import Pizzerias


class IndexView(View):
    """
    A main page view of Pizza.
    There can be two HTTP methods: GET and POST.
    """

    def get(self, request):
        """
        Returns a main page.
        """
        return render(request, 'pizza/index.html')

    def post(self, request):
        """
        Gets a POST request with data of a new order from AJAX,
        adds it to the database and calls sending to a pizzeria class.
        Returns JSON with a slug, that jQuery uses to redirecting.
        """
        # Getting information
        orderer_name = request.POST['name']
        orderer_phone_number = request.POST['phone_number']
        orderer_address = request.POST['address']
        pizza = request.POST['pizza']
        drink = request.POST['drink']
        pizzeria = request.POST['pizzeria']
        method_of_payment = request.POST['payment_method']
        date_of_delivery_list = re_split('\W', request.POST['delivery_date'])
        date_of_delivery = datetime(
            year=int(date_of_delivery_list[0]),
            month=int(date_of_delivery_list[1]),
            day=int(date_of_delivery_list[2]),
            hour=int(date_of_delivery_list[3]),
            minute=int(date_of_delivery_list[4])
        )

        # Adding the data to the database.
        new_order = PizzaOrder.objects.create(
            orderer_name=orderer_name,
            orderer_phone_number=orderer_phone_number,
            orderer_address=orderer_address,
            pizza=pizza,
            drink=drink,
            pizzeria=pizzeria,
            method_of_payment=method_of_payment,
            date_of_delivery=date_of_delivery
        )

        # Sending the order to a pizzeria, getting a status of it and
        # adding the status to the data in the database.
        try:
            new_order.status = Pizzerias(
                slug=new_order.slug,
                orderer_name=orderer_name,
                orderer_phone_number=orderer_phone_number,
                orderer_address=orderer_address,
                pizza=pizza,
                drink=drink,
                pizzeria=pizzeria,
                method_of_payment=method_of_payment,
                date_of_delivery=date_of_delivery,
                date_time_of_order=new_order.date_time_of_order
            ).send_order_to_pizzeria()
        except:
            new_order.status = 'There was an error in sending to the pizzeria'
        new_order.save()

        return JsonResponse({'slug': new_order.slug})


class OrderDetailView(DetailView):
    """
    A view of an order page.
    """
    template_name = 'pizza/order.html'
    context_object_name = 'order'
    queryset = PizzaOrder.objects.all()


def error(request):
    """
    A view of an error page.
    """
    return render(request, 'pizza/error.html')
