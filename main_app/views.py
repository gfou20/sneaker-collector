from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Sneaker, Location
from .forms import ReleaseForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')  

def sneakers_index(request):
  sneakers = Sneaker.objects.all()
  return render(request, 'sneakers/index.html', {'sneakers': sneakers})

def sneakers_detail(request, sneaker_id):
  sneaker = Sneaker.objects.get(id=sneaker_id)
  locations_sneaker_doesnt_have = Location.objects.exclude(id__in = sneaker.locations.all().values_list('id'))
  release_form = ReleaseForm()
  return render(request, 'sneakers/detail.html', {'sneaker': sneaker, 'release_form': release_form, 'locations': locations_sneaker_doesnt_have})

class SneakerCreate(CreateView):
  model = Sneaker
  fields = ['name', 'brand', 'description', 'color', 'price']  

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

class LocationUpdate(UpdateView):
  model = Location
  fields = ['state', 'city']

class LocationDelete(DeleteView):
  model = Location
  success_url = '/locations/'  

def assoc_location(request, sneaker_id, location_id):
  Sneaker.objects.get(id=sneaker_id).locations.add(location_id)
  return redirect('sneakers_detail', sneaker_id=sneaker_id)
