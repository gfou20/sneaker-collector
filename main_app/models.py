from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

DROP_TYPE = (
  ('GR', 'General Release'),
  ('LR', 'Limited Release'),
  ('SD', 'Shock Drop')
)

STATES = (
  ('AL', 'Alabama'),
  ('AK', 'Alaska'),
  ('AZ', 'Arizona'),
  ('AR', 'Arkansas'),
  ('CA', 'California'),
  ('CO', 'Colorado'),
  ('CT', 'Connecticut'),
  ('DE', 'Delaware'),
  ('FL', 'Florida'),
  ('GA', 'Georgia'),
  ('HI', 'Hawaii'),
  ('ID', 'Idaho'),
  ('IL', 'Illinois'),
  ('IN', 'Indiana'),
  ('IA', 'Iowa'),
  ('KS', 'Kansas'),
  ('KY', 'Kentucky'),
  ('LA', 'Louisiana'),
  ('ME', 'Maine'),
  ('MD', 'Maryland'),
  ('MA', 'Massachusetts'),
  ('MI', 'Michigan'),
  ('MN', 'Minnesota'),
  ('MS', 'Mississippi'),
  ('MO', 'Missouri'),
  ('MT', 'Montana'),
  ('NE', 'Nebraska'),
  ('NV', 'Nevada'),
  ('NH', 'New Hampshire'),
  ('NJ', 'New Jersey'),
  ('NM', 'New Mexico'),
  ('NY', 'New York'),
  ('NC', 'North Carolina'),
  ('ND', 'North Dakota'),
  ('OH', 'Ohio'),
  ('OK', 'Oklahoma'),
  ('OR', 'Oregon'),
  ('PA', 'Pennsylvania'),
  ('RI', 'Rhode Island'),
  ('SC', 'South Carolina'),
  ('SD', 'South Dakota'),
  ('TN', 'Tennessee'),
  ('TX', 'Texas'),
  ('UT', 'Utah'),
  ('VT', 'Vermont'),
  ('VA', 'Virginia'),
  ('WA', 'Washington'),
  ('WV', 'West Virginia'),
  ('WI', 'Wisconsin'),
  ('WY', 'Wyoming'),
)

# Create your models here.
class Location(models.Model):
  state = models.CharField(
    max_length=2,
    choices=STATES,
    default=STATES[31][0]
  )
  city = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("locations_detail", kwargs={"pk": self.id})

class Sneaker(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  color = models.CharField(max_length=50)
  price = models.IntegerField('Purchase Price')
  locations = models.ManyToManyField(Location)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sneakers_detail', kwargs={'sneaker_id': self.id})

  def rel_for_today(self):
    return self.release_set.filter(date=date.today()).count() >= len(DROP_TYPE)  

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

  class Meta:
    ordering = ['-date']  