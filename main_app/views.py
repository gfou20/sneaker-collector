from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sneaker, Location
from .forms import ReleaseForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')  

def sneakers_index(request):
  sneakers = Sneaker.objects.all()
  return render(request, 'sneakers/index.html', {'sneakers': sneakers})

def sneakers_detail(request, sneaker_id):
  sneaker = Sneaker.objects.get(id=sneaker_id)
  release_form = ReleaseForm()
  return render(request, 'sneakers/detail.html', {'sneaker': sneaker, 'release_form': release_form})

class SneakerCreate(CreateView):
  model = Sneaker
  fields = '__all__'  

class SneakerUpdate(UpdateView):
  model = Sneaker
  fields = ['brand','description', 'color', 'price']

class SneakerDelete(DeleteView):
  model = Sneaker
  success_url = '/sneakers/'  

def add_release(request, sneaker_id):
  form = ReleaseForm(request.POST)
  if form.is_valid():
    new_release = form.save(commit=False)
    new_release.sneaker_id = sneaker_id
    new_release.save()
  return redirect('sneakers_detail', sneaker_id=sneaker_id)

class LocationCreate(CreateView):
  model = Location
  fields = '__all__'  

class LocationList(ListView):
  model = Location

class LocationDetail(DetailView):
  model = Location
