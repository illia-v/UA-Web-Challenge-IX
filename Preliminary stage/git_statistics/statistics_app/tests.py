from django.core.urlresolvers import reverse
from django.test import TestCase


class IndexViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('index'))

    def test_index_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_showing_of_a_searching_form(self):
        self.assertContains(self.response, 'Statistics of a certain project')


class RepoDetailsViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('repo_details',
                                                args=('django', 'django')))

    def test_repo_details_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)


class TopReposViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('repos_by_stars'))

    def test_top_repos_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)
