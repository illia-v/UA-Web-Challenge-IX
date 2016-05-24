from datetime import datetime

from django.test import TestCase

from our_pizzeria.models import Order


class PizzaOrderModelTestCase(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            slug='test',
            orderer_name='Karl',
            orderer_phone_number=123456789,
            orderer_address='the world',
            pizza='pepperoni',
            drink='water',
            method_of_payment='cash',
            date_of_delivery=datetime.now(),
            date_time_of_order=datetime.now(),
            status=0
        )

    def test_order_basic(self):
        """
        Test base functionality of Order.
        """
        self.assertEqual(self.order.orderer_name, 'Karl')
        self.assertEqual(self.order.orderer_phone_number, 123456789)
        self.assertEqual(self.order.orderer_address, 'the world')
        self.assertEqual(self.order.pizza, 'pepperoni')
        self.assertEqual(self.order.drink, 'water')
        self.assertEqual(self.order.method_of_payment, 'cash')
        self.assertEqual(self.order.status, 0)
        self.assertEqual(self.order.get_status_display(), 'Processing')
