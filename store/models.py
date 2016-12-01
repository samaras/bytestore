from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.html import escape
from django.core.urlresolvers import reverse

# Create your models here.

class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True


class Store(models.Model):
	store_name = models.CharField(max_length=200)
	owner = models.ForeignKey(User)

class Category(models.Model):
	category = models.CharField(max_length=150)
	store = models.ForeignKey(Store)

	def __str__(self):
		return "%s" % self.category

class Product(models.Model):
	product_name = models.CharField(max_length=150)
	product_sku = models.CharField(max_length=50)
	category = models.ForeignKey(Category)
	stock = models.IntegerField()

	def __str__(self):
		return "%s (%s)" % (self.product_name, self.product_sku)

class Order(TimeStampedModel):
	total = models.DecimalField(max_digits=10, decimal_places=4)
	user = models.ForeignKey(User)

class ProductOrder(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	item_price = models.DecimalField(max_digits=10, decimal_places=4)
	order_status = models.BooleanField()

	def __str__(self):
		return ""

class Cart(TimeStampedModel):
	user = models.ForeignKey(User)
	store = models.ForeignKey(Store)
	is_guest = models.BooleanField()

class CartProduct(models.Model):
	cart = models.ForeignKey(Cart)
	product = models.ForeignKey(Product)
	store = models.ForeignKey(Store)
	quantity = models.IntegerField()
