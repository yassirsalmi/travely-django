from django.urls import path
from .views import add_package, all_packages, all_packages_admin, delete_package, modify_package, package_details, reserve_package

app_name = 'travely_packages_reservations'

urlpatterns = [
    path('add_package/', add_package, name='add_package'),
    path('modify/<int:reservation_id>/', modify_package, name='modify_package'),
    # path('all-packages/', all_packages, name='all_packages'),
    path('package/<int:pk>/', package_details, name='package_details'),
    path('all-packages/', all_packages, name='all_packages'),
    path('modify-package/<int:pk>/', modify_package, name='modify_package'),
    path('delete-package/<int:pk>/', delete_package, name='delete_package'),
    path('all-packages-admin/', all_packages_admin, name='all_packages_admin'),
    path('reserve-package/<int:pk>/', reserve_package, name='reserve_package'),  # Add this line
]