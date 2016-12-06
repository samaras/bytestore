from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('store.urls')),
    # url(r'^$', include('cart.urls')),
    # url(r'^$', include('accounts.urls')),
    url(r'^$', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
