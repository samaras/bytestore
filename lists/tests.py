from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

class HomePageTest(TestCase):

	def test_home_page_url_and_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
