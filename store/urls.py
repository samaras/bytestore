from django.conf.urls import url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home'),
    url(r'^$', views.stores, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
)
