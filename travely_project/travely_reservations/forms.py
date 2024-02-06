from django import forms
from .models import HotelReservation, TravelReservation

class HotelReservationForm(forms.ModelForm):
    class Meta:
        model = HotelReservation
        fields = ['start_date', 'end_date', 'credit_card_number', 'cvv', 'expiration_date']

class TravelReservationForm(forms.ModelForm):
    class Meta:
        model = TravelReservation
        fields = ['start_date', 'end_date', 'credit_card_number', 'cvv', 'expiration_date']




