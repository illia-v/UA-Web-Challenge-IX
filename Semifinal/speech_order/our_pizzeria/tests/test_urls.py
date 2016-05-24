from django.core.urlresolvers import resolve
from django.test import TestCase

from our_pizzeria.views import index


class OurPizzeriaURLsTestCase(TestCase):

    def setUp(self):
        self.index = resolve('/our_pizzeria/')

    def test_index_url_view_name_is_correct(self):
        """
        Test that a view name 'our_pizzeria:index', which is used in
        templates, relates to a url '/our_pizzeria/'.
        """
        self.assertEqual(self.index.view_name, 'our_pizzeria:index')

    def test_root_url_uses_index_view(self):
        """
        Test that the index page of the Our Pizzeria app resolves to
        the correct view function.
        """
        self.assertEqual(self.index.func, index)
