from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Sneakers</h1>')

def about(request):
  return HttpResponse('<h1>About the Sneaker Collector</h1>')  