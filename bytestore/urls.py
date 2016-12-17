from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^store/$', include('store.urls')),
    # url(r'^cart/$', include('cart.urls')),
    # url(r'^$', include('accounts.urls')),
    url(r'^$', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
