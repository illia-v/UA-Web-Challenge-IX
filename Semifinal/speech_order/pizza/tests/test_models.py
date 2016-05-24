from datetime import datetime

from django.test import TestCase

from pizza.models import PizzaOrder


class PizzaOrderModelTestCase(TestCase):

    def setUp(self):
        self.order = PizzaOrder.objects.create(
            orderer_name='Karl',
            orderer_phone_number=123456789,
            orderer_address='the world',
            pizza='pepperoni',
            drink='water',
            pizzeria='Your Pizzeria',
            method_of_payment='cash',
            date_of_delivery=datetime.now(),
            status='success'
        )

    def test_order_basic(self):
        """
        Test base functionality of PizzaOrder.
        """
        self.assertEqual(self.order.orderer_name, 'Karl')
        self.assertEqual(self.order.orderer_phone_number, 123456789)
        self.assertEqual(self.order.orderer_address, 'the world')
        self.assertEqual(self.order.pizza, 'pepperoni')
        self.assertEqual(self.order.drink, 'water')
        self.assertEqual(self.order.pizzeria, 'Your Pizzeria')
        self.assertEqual(self.order.method_of_payment, 'cash')
        self.assertEqual(self.order.status, 'success')
