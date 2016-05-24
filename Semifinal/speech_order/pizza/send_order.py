from our_pizzeria.get_order import get_order


# All supported pizzerias must be stored here
pizzerias = ['our pizzeria']


class Pizzerias:
    """
    Sends data of an order to the suitable pizzeria.
    """
    def __init__(self, slug, orderer_name, orderer_phone_number,
                 orderer_address, pizza, drink, pizzeria, method_of_payment,
                 date_of_delivery, date_time_of_order):
        self.slug = slug
        self.orderer_name = orderer_name
        self.orderer_phone_number = orderer_phone_number
        self.orderer_address = orderer_address
        self.pizza = pizza
        self.drink = drink
        if pizzeria.lower() in pizzerias:
            self.pizzeria = pizzeria
        else:
            self.pizzeria = 'our pizzeria'
        self.method_of_payment = method_of_payment
        self.date_of_delivery = date_of_delivery
        self.date_time_of_order = date_time_of_order

    def send_order_to_pizzeria(self):
        """
        Redirection to the suitable sending function.
        If sending was successful returns message about success.
        Conditions with all supported pizzerias have to be here.
        """
        if self.pizzeria == 'our pizzeria':
            self.our_pizzeria()
            return 'The order was sent to Our Pizzeria'

    def our_pizzeria(self):
        """
        Sending an order to Our Pizzeria.
        """
        get_order(
            slug=self.slug,
            orderer_name=self.orderer_name,
            orderer_phone_number=self.orderer_phone_number,
            orderer_address=self.orderer_address,
            pizza=self.pizza,
            drink=self.drink,
            method_of_payment=self.method_of_payment,
            date_of_delivery=self.date_of_delivery,
            date_time_of_order=self.date_time_of_order
        )
