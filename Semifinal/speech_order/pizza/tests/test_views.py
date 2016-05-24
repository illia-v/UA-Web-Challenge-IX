from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from pizza.models import PizzaOrder


class PizzaOrderBaseTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.order = PizzaOrder.objects.create(
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


class IndexViewTestCase(PizzaOrderBaseTestCase):

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses the
        correct template.
        """
        with self.assertTemplateUsed('pizza/index.html'):
            response = self.client.get(reverse('pizza:index'))
            self.assertEqual(response.status_code, 200)


class OrderDetailViewTestCase(PizzaOrderBaseTestCase):

    def test_order_detail_view_basic(self):
        """
        Test that order detail view returns a 200 response, uses
        the correct template and has the correct context.
        """
        with self.assertTemplateUsed('pizza/order.html'):
            response = self.client.get(reverse(
                'pizza:order_detail',
                kwargs={'slug': self.order.slug}
            ))
            self.assertEqual(response.status_code, 200)
        order_data = response.context_data['order']
        self.assertEqual(order_data.orderer_name, 'Karl')
        self.assertEqual(order_data.orderer_phone_number, 123456789)
        self.assertEqual(order_data.orderer_address, 'the world')
        self.assertEqual(order_data.pizza, 'pepperoni')
        self.assertEqual(order_data.drink, 'water')
        self.assertEqual(order_data.pizzeria, 'Your Pizzeria')
        self.assertEqual(order_data.method_of_payment, 'cash')


class ErrorViewTestCase(TestCase):

    def test_error_view_basic(self):
        """
        Test that error view returns a 200 response and uses the
        correct template.
        """
        with self.assertTemplateUsed('pizza/error.html'):
            response = self.client.get(reverse('pizza:error'))
            self.assertEqual(response.status_code, 200)
