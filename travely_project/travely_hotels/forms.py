from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'location', 'stars', 'pool', 'room_types', 'price_per_night', 'image']

    widgets = {
        'room_types': forms.CheckboxSelectMultiple(),
    }
