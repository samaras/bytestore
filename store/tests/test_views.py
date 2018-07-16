from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage

from store.models import Store
from store.views import home_page
        
        
class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
	
	def test_store_view(self):
		resp = self.client.get('/store/')
		self.assertEqual(resp.status_code, 200)
		
	def test_product_view(TestCase):
		resp = self.client.get('/product/')
		self.assertEqual(resp.status_code, 200)
		
	def test_category_view(TestCase):
		resp = self.client.get('/category/')
		self.assertEqual(resp.status_code, 200)
	
	def test_cart_view(TestCase):
		resp = self.client.get('/cart/')
		self.assertEqual(resp.status_code, 200)
		
class StorePageTest(TestCase):
    """Test the /store page with one and two shops entries"""

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create(username='samaras', )

        def test_one_store(self):
            Store.objects.create(store_name='1-Mart', owner=self.user)
            response = self.client.get('/store')
            self.assertContains(response, '1-Mart')

        def test_two_store(self):
            Store.objects.create(store_name='1-Mart', owner=self.user)
            Store.objects.create(store_name='2-Mart', owner=self.user)
            response. = self.client.get('/store')
            self.assertContains(response, '1-Mart')
            self.assertContains(response, '2-Mart')

        def test_no_stores(self):
            response = self.client.get('/store')
            self.assertContains(response, 'No stores available yet')

class StoreModelTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create(username='foo')

    def test_saving_and_retrieving_store(self):
        self.client.login(username='foo', password='bar')


        first_store = Store()
        first_store.store_name = 'Computer Mart'
        first_store.owner = self.user
        
        second_store = Store()
        second_store.store_name = 'Star Shop'
        second_store.owner = self.user
        
        saved_stores = Store.objects.all()
        self.assertEqual(saved_stores.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.store_name, 'Computer Mart')
        self.assertEqual(second_saved_item.store_name, 'Star Shop')
        
class TestStaticFiles(TestCase):
    """Check if app contains required static files"""
    def test_images(self):
        abs_path = finders.find('logo.png')
        self.assertIsNotNone(abs_path)
        abs_path = finders.find('apple-touch-icon.png')
        self.assertIsNotNone(abs_path)

    def test_css(self):
        abs_path = finders.find('css/main.css')
        self.assertIsNotNone(abs_path)
        abs_path = finders.find('libs/bootstrap-3.3.5/css/bootstrap.css')
        self.assertIsNotNone(abs_path)
        abs_path = finders.find('libs/font-awesome-4.3.0/css/font-awesome.css')
        self.assertIsNone(abs_path)