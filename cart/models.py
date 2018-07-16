from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from store.models import Product, Store, TimeStampedModel, Category

# Create your models here.

class Cart(TimeStampedModel):
	user = models.ForeignKey(User, verbose_name=_("Customer"), null=True)
	store = models.ForeignKey(Store, verbose_name=_("Store Name"))
	is_guest = models.BooleanField(verbose_name=_("Guest?"), default=True)
	products = models.ManyToManyField(Product, through='CartProduct')

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return u"%s %s" % (self.user.first_name, self.user.last_name)

class CartProduct(models.Model):
	cart = models.ForeignKey(Cart, verbose_name=_("Cart"))
	product = models.ForeignKey(Product, verbose_name=_("Product Name"))
	store = models.ForeignKey(Store, verbose_name=_("Store Name"))
	quantity = models.PositiveSmallIntegerField(verbose_name=_("Quantity"))
	date_added = models.DateTimeField(auto_now_add=True)

	def total(self):
		return self.quantity * self.product.price

	def name(self):
		return self.product.product_name

	def price(self):
		return self.product.price