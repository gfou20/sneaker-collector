from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sneaker, Location
from .forms import ReleaseForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')  

@login_required
def sneakers_index(request):
  sneakers = Sneaker.objects.filter(user=request.user)
  return render(request, 'sneakers/index.html', {'sneakers': sneakers})

@login_required
def sneakers_detail(request, sneaker_id):
  sneaker = Sneaker.objects.get(id=sneaker_id)
  locations_sneaker_doesnt_have = Location.objects.exclude(id__in = sneaker.locations.all().values_list('id'))
  release_form = ReleaseForm()
  return render(request, 'sneakers/detail.html', {'sneaker': sneaker, 'release_form': release_form, 'locations': locations_sneaker_doesnt_have})

class SneakerCreate(LoginRequiredMixin, CreateView):
  model = Sneaker
  fields = ['name', 'brand', 'description', 'color', 'price']  

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SneakerUpdate(LoginRequiredMixin, UpdateView):
  model = Sneaker
  fields = ['brand','description', 'color', 'price']

class SneakerDelete(LoginRequiredMixin, DeleteView):
  model = Sneaker
  success_url = '/sneakers/'  

@login_required
def add_release(request, sneaker_id):
  form = ReleaseForm(request.POST)
  if form.is_valid():
    new_release = form.save(commit=False)
    new_release.sneaker_id = sneaker_id
    new_release.save()
  return redirect('sneakers_detail', sneaker_id=sneaker_id)

class LocationCreate(LoginRequiredMixin, CreateView):
  model = Location
  fields = '__all__'  

class LocationList(LoginRequiredMixin, ListView):
  model = Location

class LocationDetail(LoginRequiredMixin, DetailView):
  model = Location

class LocationUpdate(LoginRequiredMixin, UpdateView):
  model = Location
  fields = ['state', 'city']

class LocationDelete(LoginRequiredMixin, DeleteView):
  model = Location
  success_url = '/locations/'  

@login_required
def assoc_location(request, sneaker_id, location_id):
  Sneaker.objects.get(id=sneaker_id).locations.add(location_id)
  return redirect('sneakers_detail', sneaker_id=sneaker_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('sneakers_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
