from django.test.client import Client 
from django.test.client import RequestFactory
from django.test import TestCase
from store.models import Store
from django.contrib.auth.models import User
from store.views import StoreListView

class StoreListViewTests(TestCase):
	""" Store list view tests """

	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='foo', password='bar', email='foo@bar.com')
		self.user.save()

	def test_store_in_the_context(self):
		
		response = self.client.get('/store')
		self.assertEquals(list(response.context['objects_list']), [])

		Store.objects.create(store_name='KMart', owner=self.user)
		response = client.get('/store')
		self.assertEquals(response.context['objects_list'].count(), 1)

	def test_stores_in_the_context_request_factory(self):

		factory = RequestFactory()
		request = factory.get('/')

		response = StoreListView.as_view()(request)

		self.assertEquals(list(response.context_data['objects_list']), [])

		Store.objects.create(store_name='KMart', owner=self.user)
		self.assertEquals(response.context_data['objects_list'].count(), 1)