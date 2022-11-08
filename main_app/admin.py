from django.contrib import admin
from .models import Sneaker, Release, Location

# Register your models here.
admin.site.register(Sneaker)
admin.site.register(Release)
admin.site.register(Location)