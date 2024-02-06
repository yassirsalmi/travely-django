from django.urls import path
from .views import goto_hotel_reservation, goto_travel_reservation,travel_reservation,hotel_reservation

app_name = 'travely_reservations'

urlpatterns = [
    path('hotel-reservation/<int:hotel_id>/', goto_hotel_reservation, name='goto_hotel_reservation'),
    path('travel-reservation/<int:travel_id>/', goto_travel_reservation, name='goto_travel_reservation'),
    path('travel-reservation-done/<int:travel_id>/', travel_reservation, name='travel_reservation'),
    path('hotel-reservation-done/<int:hotel_id>/', hotel_reservation, name='hotel_reservation'),
]

