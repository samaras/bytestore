from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from store.models import Store, Product, Category

class StoreListView(ListView):
	model = Store
	template_name = 'store_list.html'

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
