from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _ 

from accounts.models import Profile

# Register your models here.

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = _('Profiles')

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
