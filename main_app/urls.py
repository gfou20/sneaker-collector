from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sneakers/', views.sneakers_index, name='sneakers_index'),
  path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='sneakers_detail'),
]