from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>Bytestore</title></html>')

