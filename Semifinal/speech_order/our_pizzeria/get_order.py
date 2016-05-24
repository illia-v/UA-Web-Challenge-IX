from .models import Order


def get_order(slug, orderer_name, orderer_phone_number, orderer_address,
              pizza, drink, method_of_payment, date_of_delivery,
              date_time_of_order):
    """
    Gets information of an order and adds it to the database.
    """
    Order.objects.create(
        slug=slug,
        orderer_name=orderer_name,
        orderer_phone_number=orderer_phone_number,
        orderer_address=orderer_address,
        pizza=pizza,
        drink=drink,
        method_of_payment=method_of_payment,
        date_of_delivery=date_of_delivery,
        date_time_of_order=date_time_of_order,
        status=0
    )
