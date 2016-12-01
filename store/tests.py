from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.contrib.auth.models import User

from store.models import Store
from store.views import home_page


# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page_url_and_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn(b'Byte Store</title>', response.content)
        
class StoreModelTest(TestCase):

    def test_saving_and_retrieving_store(self):
        first_store = Store()
        first_store.store_name = 'Computer Mart'
        first_store.owner = User()
        
        second_store = Store()
        second_store.store_name = 'Star Shop'
        second_store.owner = User()
        
        saved_stores = Store.objects.all()
        self.assertEqual(saved_stores.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.store_name, 'Computer Mart')
        self.assertEqual(second_saved_item.store_name, 'Star Shop')
        

