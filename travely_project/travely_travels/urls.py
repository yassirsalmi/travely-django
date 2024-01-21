from django.urls import path
from .views import add_travel, add_promotion, add_category,all_travels,modify_travel,delete_travel,travel_details

app_name = 'travely_travels'

urlpatterns = [
    path('add_travel/', add_travel, name='add_travel'),
    path('add_promotion/', add_promotion, name='add_promotion'),
    path('add_category/', add_category, name='add_category'),
    path('all_travels/', all_travels, name='all_travels'),
    path('modify_travel/<int:travel_id>/', modify_travel, name='modify_travel'),
    path('delete_travel/<int:travel_id>/', delete_travel, name='delete_travel'),
    path('travel_details/<int:travel_id>/', travel_details, name='travel_details'),
]
