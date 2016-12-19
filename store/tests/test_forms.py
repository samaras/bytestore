from django.test.client import Client 
from django.test.client import RequestFactory
from django.test import TestCase
from .models import Store
from django.contrib.auth.models import User

class StoreListViewTests(TestCase):
	""" Store list view tests """

	def test_store_in_the_context(self):

		# TODO: Remove this nonsense
		user = User.get(1) # admin

		client = Client()
		response = client.get('/store')

		self.assertEquals(list(response.context['object_list']), [])

		Store.objects.create(store_name='KMart', owner=user)
		response = client.get('/store')
		self.assertEquals(response.context['object_list'].count(), 1)

	def test_stores_in_the_context_request_factory(self):

		# TODO: Remove this soon
		user = User.get(1) # admin

		factory = RequestFactory()
		request = factory.get('/')

		response = StoreListView.as_view()(request)

		self.assertEquals(list(response.context_data['object_list']), [])

		Store.objects.create(store_name='KMart', owner=user)
		self.assertEquals(response.context_data['object_list'].count(), 1)