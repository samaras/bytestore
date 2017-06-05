from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts.views import *

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^accounts/register/$', register),
	url(r'^accounts/profile/$', profile),
	url(r'^$', include('django.contrib.auth.urls')),
	# url(r'^register/success/$', accounts.register_success),
    url(r'^store/$', include('store.urls')),
    # url(r'^cart/$', include('cart.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
