from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Profile(models.Model):
	""" User profile  """
	user = models.OneToOneField(User, related_name="profile", verbose_name=_("user"), on_delete="cascade")
	activation_key = models.CharField(max_length=255)
	expires = models.DateTimeField()
	is_customer = models.BooleanField(default=True, verbose_name=_("store_owner"))

	class Meta:
		verbose_name_plural = _("profiles")

	def __unicode__(self):
		return u"%s %s" % (self.user.first_name, self.user.last_name) 		