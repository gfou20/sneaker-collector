from django.db import models

# Create your models here.
class Sneaker(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  color = models.CharField(max_length=50)

  def __str__(self):
    return self.name