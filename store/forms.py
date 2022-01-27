from django import forms
from store.models import Cloths


class StoreForm(forms.ModelForm):
  class Meta:
    model = Cloths
    fields = ("__all__")