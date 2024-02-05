from django.shortcuts import get_object_or_404, render, redirect
from travely_hotels.models import Hotel
from travely_reservations.models import HotelReservation, TravelReservation
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .forms import UserProfileForm, CustomPasswordChangeForm
from django.views import View
from .models import Client, CustomUser
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from travely_travels.models import Travel
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('user_profile')


def home(request):
    return render(request, 'travely_auth/home.html')


def user_profile(request):
    return render(request, 'travely_auth/user_profile.html')    

def about_page_view(request):
    return render(request, 'travely_auth/about_page.html')  


@login_required(login_url="/login")
def services_page_view(request):
    return render(request, 'travely_auth/services_page.html')  



# admin views

def is_admin(user):
    return user.is_authenticated and user.is_admin

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
     return render(request, 'admin/admin_dashboard.html')



######################



@user_passes_test(is_admin, login_url='/login/')
def admin_dashboard(request):
    users = CustomUser.objects.filter(is_admin=True) | CustomUser.objects.filter(is_client=True)
    # Exclude the superuser
    users = users.exclude(is_superuser=True)

    context = {'users': users}
    return render(request, 'travely_auth/../admin/admin_dashboard.html', context)

########################


@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    template_name = 'travely_auth/user_profile.html'

    def get(self, request):
        form = UserProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        return render(request, self.template_name, {'form': form})



def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_visitor = False
            user.is_client = True
            user.save()
            login(request, user)
            return redirect('travely_auth/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})




def home(request):
    travels = Travel.objects.all()
    hotels = Hotel.objects.all()
    return render(request, 'travely_auth/home.html', {'travels': travels, 'hotels':hotels})


def all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'travely_auth/all_users.html', {'users': users})



def delete_user(request, user_id):
    User = get_user_model()
    user = get_object_or_404(CustomUser, pk=user_id)

    # Perform deletion
    user.delete()

    # Redirect to the page where all users are listed
    return redirect('travely_auth/all_users')



def client_dashboard(request):
    # Assuming the currently logged-in user is accessible via `request.user`
    user = request.user

    # Fetch hotel reservations for the current user
    hotel_reservations = HotelReservation.objects.filter(user=user)

    # Fetch travel reservations for the current user
    travel_reservations = TravelReservation.objects.filter(user=user)

    return render(request, 'client/client_dashboard.html', {'hotel_reservations': hotel_reservations, 'travel_reservations': travel_reservations})



########### search

# views.py

def search_results(request):
    query = request.GET.get('query')
    if query:
        travels = Travel.objects.filter(title__icontains=query)
        hotels = Hotel.objects.filter(name__icontains=query)
    else:
        travels = Travel.objects.none()
        hotels = Hotel.objects.none()
    return render(request, 'travely_auth/search_results.html', {'travels': travels, 'hotels': hotels})


