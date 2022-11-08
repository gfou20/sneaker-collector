from django.forms import ModelForm
from .models import Release

class ReleaseForm(ModelForm):
  class Meta:
    model = Release
    fields = ['date', 'drop_type']