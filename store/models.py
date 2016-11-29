from django.db import models
from django.auth import User

# Create your models here.

class Store(models.Model):
	name = models.CharField(max_length=200)
	owner = models.ForeignKey(User)

class Category(models.Model):
	category = models.CharField(max_length=150)
	store = models.ForeignKey(Store)

class Product(models.Model):
	product_name = models.CharField(max_length=150)
	product_sku = models.CharField(max_length=50)
	category = models.ForeignKey(Category)
	stock = models.IntegerField()

class Order(models.Model):
	total = models.DecimalField(max_digits=10, decimal_places=4)
	date_added = models.DateTimeField()
	user = models.ForeignKey(User)

class ProductOrder(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	item_price = models.DecimalField(max_digits=10, decimal_places=4)
	order_status = models.BooleanField()

class Cart(models.Model):
	user = models.ForeignKey(User)
	store = models.ForeignKey(Store)
	date_added = models.DateTimeField()
	date_updated = models.DateTimeField()
	is_guest = models.BooleanField()

class CartProduct(models.Model):
	cart = models.ForeignKey(Cart)
	product = models.ForeignKey(Product)
	store = models.ForeignKey(Store)
	quantity = models.IntegerField()
	date_added = models.DateTimeField()
