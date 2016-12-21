from django.test import TestCase
from django.test.client import Client
from store.models import Store, Product, Category
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class StoreAndProductModelsTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='foo', password='bar', email='foo@bar.com')
		self.user.save()
		self.client = Client()

	def test_cannot_save_empty_category_store_product(self):
		store_ = Store(store_name='Mart', owner=self.user)
		store_.save()

		category_ = Category(category='Fruits', store=store_)
		category_.save()

		product = Product(product_name='', product_sku='SKU', category=category_, qty_stock=0, price=10.00)

		with self.assertRaises(ValidationError):
			product.save()