from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def stores(request):
	return render(request, '<html><body></body></html>')
