from django.test import TestCase
from store.models import Store, Product, Category
from django.core.exceptions import ValidationError

class StoreAndProductModelsTest(TestCase):
	
	def test_cannot_save_empty_category_store_product(self):
		store_ = Store(store_name='Mart', owner=1)
		category_ = Category(category='', store=store_)
		product = Product(product_name='', product_sku='SKU', category=category_, stock=0)

		with self.assertRaises(ValidationError):
			product.save()