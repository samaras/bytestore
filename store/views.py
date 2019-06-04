from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Store, Product, Category

"""class RestrictToLoggedInUserMixin(self):
	Add a restriction that the logged in user can only objects belonging to them 
	def get_queryset(self):
		queryset = super(RestrictToLoggedInUserMixin, self).get_queryset()
		queryset = queryset.filter(user=self.request.user)
		return queryset"""

class StoreListView(ListView):
	queryset = Store.objects.order_by('store_name')
	template_name = 'store_list.html'
	context_object_name = 'store_list'

class StoreDetail(DetailView):
	context_object_name = 'store'
	queryset = Store.objects.all()

	def get_context_data(self, **kwargs):
		context = super(StoreDetail, self).get_context_data(**kwargs)
		context['product_list'] = Product.objects.all()
		return context

class StoreCreateView(CreateView):
	model = Store 
	fields = ['store_name']
	template_name = 'store_form.html'

	def get_success_url():
		return reverse('stores')

	def get_context_data(self, **kwargs):
		context = super(StoreCreateView, self).get_context_data(**kwargs)
		context['action'] = reverse('store-new')

		return context

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(StoreCreate, self).form_valid(form)

class StoreUpdateView(UpdateView):
	model = Store
	fields = ['store_name']
	template_name = 'store_form.html'

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(StoreCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse('stores')

	def get_context_data(self, **kwargs):
		context = super(StoreUpdateView, self).get_context_data(**kwargs)
		context['action'] = reverse('store-edit', kwargs={'pk': self.get_object().id})

		return context


class StoreDeleteView(DeleteView):
	model = Store
	success_url = reverse_lazy('stores')


# Products views 

class ProductListView(ListView):
	model = Product

class ProductCreateView(CreateView):
	model = Product

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def stores(request):
	return render(request, '<html><body></body></html>')
