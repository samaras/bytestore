from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from store.models import Store

class StoreListView(ListView):
	model = Store

class StoreCreate(CreateView):
	model = Store 
	fields = ['store_name']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(StoreCreate, self).form_valid(form)

class StoreUpdate(UpdateView):
	model = Store
	fields = ['store_name']

class StoreDelete(DeleteView):
	model = Store
	success_url = reverse_lazy('store-list')

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def stores(request):
	return render(request, '<html><body></body></html>')
