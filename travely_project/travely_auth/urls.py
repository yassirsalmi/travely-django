from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about_page_view, name='about_page'),
    path('services', views.services_page_view, name='services_page'),
    path('sign-up', views.sign_up, name='sign_up'),
]
