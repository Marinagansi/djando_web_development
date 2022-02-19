from django import forms
from booking.models import Booking


class BookedForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields=("__all__")
   
    

class BookingUpdateForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ('email','start_date','days') 