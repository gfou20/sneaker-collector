from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('sneakers/', views.sneakers_index, name='sneakers_index'),
  path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='sneakers_detail'),
  path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
  path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
  path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
  path('sneakers/<int:sneaker_id>/add_release/', views.add_release, name='add_release'),
  path('sneakers/<int:sneaker_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),
  path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
  path('locations/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
  path('locations/', views.LocationList.as_view(), name='locations_index'),
  path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
  path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
  path('accounts/signup', views.signup, name='signup')
]