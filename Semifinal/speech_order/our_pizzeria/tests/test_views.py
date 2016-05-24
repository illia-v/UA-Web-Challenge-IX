from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from our_pizzeria.models import Order


class OrderBaseTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.order = Order.objects.create(
            slug='testslug',
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


class IndexViewTestCase(OrderBaseTestCase):

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses the
        correct template.
        """
        with self.assertTemplateUsed('our_pizzeria/index.html'):
            response = self.client.get(reverse('our_pizzeria:index'))
            self.assertEqual(response.status_code, 200)


class OrderDetailViewTestCase(OrderBaseTestCase):

    def test_order_detail_view_basic(self):
        """
        Test that order detail view returns a 200 response, uses
        the correct template and has the correct context.
        """
        with self.assertTemplateUsed('our_pizzeria/order.html'):
            response = self.client.get(reverse(
                'our_pizzeria:order',
                kwargs={'slug': self.order.slug}
            ))
            self.assertEqual(response.status_code, 200)
        order_data = response.context_data['order']
        self.assertEqual(order_data.get_status_display(), 'Processing')
