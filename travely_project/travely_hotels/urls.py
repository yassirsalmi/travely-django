from django.urls import path
from .views import add_hotel, all_hotels, hotel_details, modify_hotel, delete_hotel

app_name = 'travely_hotels'

urlpatterns = [
    path('add/', add_hotel, name='add_hotel'),
    path('all_hotels/', all_hotels, name='all_hotels'),
    path('modify_hotel/<int:hotel_id>/', modify_hotel, name='modify_hotel'),
    path('delete_hotel/<int:hotel_id>/', delete_hotel, name='delete_hotel'),
    path('hotel/<int:hotel_id>/', hotel_details, name='hotel_details'),
    
    
]