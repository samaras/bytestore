from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^/$', views.home_page, name='home'),
    url(r'^$', views.stores, name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',{'template_name': 'store/category.html'}, name='catelog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product',{'template_name': 'store/product.html'}, name='catelog_product'),
    url(r'^store/$', views.StoreListView.as_view(), name='stores'),
    url(r'^store/create/$', views.StoreCreateView.as_view(), name='store-new'),
    url(r'^store/edit/(?P<pk>\d+)/$', views.StoreUpdateView.as_view(), name='store-new'),
    url(r'^store/delete/(?P<pk>\d+)/$', views.StoreDeleteView.as_view(), name='store-delete'),
)
