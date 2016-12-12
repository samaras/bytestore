from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.html import escape
from django.core.urlresolvers import reverse
from django import forms

from django.utils import timezone
import datetime
import decimal

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
		verbose_name_plural = _("Store's")
		permissions = (
			("view_store", "Can view stores"),
		)

	def __unicode__(self, user):
		return self.store_name

	def is_owner(self):
		owner = self.owner == user.id
		return owner

class Category(TimeStampedModel):
	category = models.CharField(max_length=150, verbose_name=_("Category"))
	store = models.ForeignKey(Store, verbose_name=_("Store Name"))
	slug = models.SlugField(max_length=50, unique=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		db_table = 'store_categories'
		unique_together = ('category', 'store')
		ordering = ['-created']
		verbose_name_plural = _("Categories")

	def __unicode__(self):
		return self.category

	@models.permalink
	def get_absolute_url(self):
		return ('catalog_category', (), { 'category_slug': self.slug })

class Product(models.Model):
	product_name = models.CharField(max_length=150, verbose_name=_("Product Name"))
	product_sku = models.CharField(max_length=50, verbose_name=_("Product SKU"), unique=True)
	category = models.ForeignKey(Category, verbose_name=_("Category"))
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
	qty_stock = models.IntegerField(verbose_name=_("Stock Quantity"))
	product_image = models.ImageField(upload_to='images/products')
	product_status = models.BooleanField(default=True)
	description = models.TextField()
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return u"%s (%s)" % (self.product_name, self.product_sku)

	@models.permalink
	def get_absolute_url(self):
		return ('catalog_product', (), { 'product_slug': self.slug })

class Order(TimeStampedModel):
	PROCESSED 	= 1
	SHIPPED 	= 2
	CANCELLED	= 3

	ORDER_STATUSES = ((PROCESSED, 'Processed'), (SHIPPED, 'Shipped'), (CANCELLED, 'Cancelled'))

	total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Price"))
	user = models.ForeignKey(User, verbose_name=_("Customer"), null=True)
	status = models.IntegerField(choices=ORDER_STATUSES)
	transaction_id = models.CharField(max_length=20)
	products = models.ManyToManyField(Product, through='OrderProduct')

	# shipping information
	shipping_address1 = models.CharField(max_length=50)
	shipping_address2 = models.CharField(max_length=50)
	shipping_city 	  = models.CharField(max_length=50)

	class Meta:
		verbose_name = _("Order")
		verbose_name_plural = _("Orders")
		ordering = ["created"]

	def was_ordered_recently(self):
		return self.created >= timezone.now - datetime.timedelta(days=3)

	@property
	def total(self):
		total = decimal.Decimal('0.00')
		order_items = OrderProduct.objects.filter(order=self)

		for product in order_items:
			total += item.total
		return total
	

class OrderProduct(models.Model):
	order = models.ForeignKey(Order, verbose_name=_("Order"))
	product = models.ForeignKey(Product, verbose_name=_("Product Name"))
	quantity = models.SmallIntegerField(verbose_name=_("Quantity"), default=1)
	item_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
