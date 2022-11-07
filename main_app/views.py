from django.shortcuts import render
from django.http import HttpResponse

class Sneaker:  
  def __init__(self, name, brand, description, color):
    self.name = name
    self.brand = brand
    self.description = description
    self.color = color

sneakers = [
  Sneaker('Taxi', 'Jordan', 'Jordan 1 silhoutte', 'Yellow'),
  Sneaker('Pollen', 'Jordan', 'Jordan 1 silhoutte', 'Dark_Yellow'),
  Sneaker('Tokyo', 'Jordan', 'Jordan 1 silhoutte', 'Silver'),
  Sneaker('Off_White', 'Jordan', 'Jordan 1 silhoutte', 'Red, Black, White')
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Sneakers</h1>')

def about(request):
  return render(request, 'about.html')  

def sneakers_index(request):
  return render(request, 'sneakers/index.html', {'sneakers': sneakers})