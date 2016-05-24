from django.core.urlresolvers import resolve
from django.test import TestCase

from pizza.views import error, IndexView


class PizzaURLsTestCase(TestCase):

    def setUp(self):
        self.index = resolve('/pizza/')
        self.error = resolve('/pizza/error/')

    def test_index_url_view_name_is_correct(self):
        """
        Test that a view name 'pizza:index', which is used in templates,
        relates to a url '/pizza/'.
        """
        self.assertEqual(self.index.view_name, 'pizza:index')

    def test_error_url_view_name_is_correct(self):
        """
        Test that a view name 'pizza:error', which is used in templates,
        relates to a url '/pizza/error/'.
        """
        self.assertEqual(self.error.view_name, 'pizza:error')

    def test_index_url_uses_index_view(self):
        """
        Test that the index page of the Pizza app resolves to the
        correct view function.
        """
        self.assertEqual(self.index.func.__name__, IndexView.__name__)

    def test_error_url_uses_error_view(self):
        """
        Test that the error page of the Pizza app resolves to the
        correct view function.
        """
        self.assertEqual(self.error.func, error)
