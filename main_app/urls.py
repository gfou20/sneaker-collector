from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sneakers/', views.sneakers_index, name='sneakers_index'),
  path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='sneakers_detail'),
  path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
  path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
  path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
  path('sneakers/<int:sneaker_id>/add_release/', views.add_release, name='add_release'),
]