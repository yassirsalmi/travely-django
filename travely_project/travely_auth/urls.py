from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about_page_view, name='about_page'),
    path('services', views.services_page_view, name='services_page'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('user-profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('admin-dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('all_users/', views.all_users, name='all_users'), 
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),


]
