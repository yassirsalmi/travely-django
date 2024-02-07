from django import forms
from .models import PackageReservation

class PackageReservationForm(forms.ModelForm):
    class Meta:
        model = PackageReservation
        fields = ['package_name','start_point', 'end_point', 'departure_date', 'return_date', 'hotel_name', 'duration_of_stay', 'city_image', 'hotel_image', 'price']


from .models import ReservationProcess

class ReservationProcessForm(forms.ModelForm):
    class Meta:
        model = ReservationProcess
        fields = ['credit_card_number', 'cvv', 'expiration_date']