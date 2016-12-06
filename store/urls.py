from django.conf.urls import url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home'),
    url(r'^$', views.stores, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',{'template_name': 'store/category.html'}, name='catelog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product',{'template_name': 'store/product.html'}, name='catelog_product')
)
