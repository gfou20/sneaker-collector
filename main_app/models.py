from django.db import models
from django.urls import reverse

DROP_TYPE = (
  ('GR', 'General Release'),
  ('LR', 'Limited Release'),
  ('SD', 'Shock Drop')
)

# Create your models here.
class Sneaker(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  color = models.CharField(max_length=50)
  price = models.IntegerField('Purchase Price')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sneakers_detail', kwargs={'sneaker_id': self.id})

class Release(models.Model):
  date = models.DateField('Release Date')
  drop_type = models.CharField(
    max_length=2,
    choices=DROP_TYPE,
    default=DROP_TYPE[0][0]
  )  
  sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_drop_type_display()} on {self.date}"