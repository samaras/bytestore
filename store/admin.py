from django.contrib import admin
from store.models import Store, Product, Category, Order, OrderProduct

# Register your models here.

admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
