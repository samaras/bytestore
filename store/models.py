from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.html import escape
from django.core.urlresolvers import reverse

from django.utils import timezone
import datetime

# Create your models here.

class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created On"))
	modified = models.DateTimeField(auto_now = True, verbose_name=_("Modified On"))

	class Meta:
		abstract = True


class Store(models.Model):
	store_name = models.CharField(max_length=200, unique=True, verbose_name=_("Store Name"))
	owner = models.ForeignKey(User, verbose_name=_("Store Owner"))

	class Meta:
		verbose_name = _("Store")
		verbose_name_plural = _("Store's")

	def __unicode__(self):
		return self.store_name

class Category(models.Model):
	category = models.CharField(max_length=150, verbose_name=_("Category"))
	store = models.ForeignKey(Store, verbose_name=_("Store Name"))

	class Meta:
		verbose_name = _("Product")
		verbose_name_plural = _("Products")

	def __unicode__(self):
		return "%s" % self.category

class Product(models.Model):
	product_name = models.CharField(max_length=150, verbose_name=_("Product Name"))
	product_sku = models.CharField(max_length=50, verbose_name=_("Product SKU"), unique=True)
	category = models.ForeignKey(Category, verbose_name=_("Category"))
	stock = models.IntegerField(verbose_name=_("Stock Quantity"))

	class Meta:
		verbose_name = _("Product")
		verbose_name_plural = _("Products")

	def __unicode__(self):
		return "%s (%s)" % (self.product_name, self.product_sku)

class Order(TimeStampedModel):
	total = models.DecimalField(max_digits=10, decimal_places=4, verbose_name=_("Total Price"))
	user = models.ForeignKey(User, verbose_name=_("Customer"))

	class Meta:
		verbose_name = _("Order")
		verbose_name_plural = _("Orders")
		ordering = ["created"]

	def was_ordered_recently(self):
		return self.created >= timezone.now - datetime.timedelta(days=3)

class ProductOrder(models.Model):
	order = models.ForeignKey(Order, verbose_name=_("Order"))
	product = models.ForeignKey(Product, verbose_name=_("Product Name"))
	quantity = models.IntegerField(verbose_name=_("Quantity"))
	item_price = models.DecimalField(max_digits=10, decimal_places=4, verbose_name=_("Price"))


class Cart(TimeStampedModel):
	user = models.ForeignKey(User, verbose_name=_("Customer"))
	store = models.ForeignKey(Store, verbose_name=_("Store Name"))
	is_guest = models.BooleanField(verbose_name=_("Guest?"))

	class Meta:
		verbose_name = _("Cart")
		verbose_name_plural = _("Carts")

	def __unicode__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

class CartProduct(models.Model):
	cart = models.ForeignKey(Cart, verbose_name=_("Cart"))
	product = models.ForeignKey(Product, verbose_name=_("Product Name"))
	store = models.ForeignKey(Store, verbose_name=_("Store Name"))
	quantity = models.IntegerField(verbose_name=_("Quantity"))

    
