from django.shortcuts import get_object_or_404, render, redirect
from travely_hotels.models import Hotel

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
from travely_packages_reservations.models import PackageReservation, ReservationProcess
from travely_reservations.models import HotelReservation, TravelReservation


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
            return redirect('travely_auth:home')
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


@login_required
def client_dashboard(request):
    user = request.user
    hotel_reservations = HotelReservation.objects.filter(user=user)
    travel_reservations = TravelReservation.objects.filter(user=user)
    package_reservations = ReservationProcess.objects.filter(user=user)
    return render(request, 'client/client_dashboard.html', {'hotel_reservations': hotel_reservations, 'travel_reservations': travel_reservations, 'package_reservations': package_reservations})


########### search

def search_results(request):
    query = request.GET.get('query')
    if query:
        travels = Travel.objects.filter(title__icontains=query)
        hotels = Hotel.objects.filter(name__icontains=query)
    else:
        travels = Travel.objects.none()
        hotels = Hotel.objects.none()
    return render(request, 'travely_auth/search_results.html', {'travels': travels, 'hotels': hotels})




####################### admin views
from django.db.models import Sum
def is_admin(user):
    return user.is_authenticated and user.is_admin

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
     return render(request, 'admin/admin_dashboard.html')

@login_required
@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    user.delete()
    return redirect('travely_auth/all_users')

@user_passes_test(is_admin, login_url='/login/')
def admin_dashboard(request):
    users = CustomUser.objects.filter(is_admin=True) | CustomUser.objects.filter(is_client=True)
    users = users.exclude(is_superuser=True)

    user_expenses = get_user_expenses()

    xValues = [user.username for user in users]
    yValues = [float(user_expenses.get(user.id, 0)) for user in users] 
    barColors = ["red", "green", "blue", "orange", "brown"]  

    print(xValues)
    print(yValues)

    context = {
        'xValues': xValues,
        'yValues': yValues,
        'barColors': barColors
    }
    print(context['xValues'])
    return render(request, 'travely_auth/../admin/admin_dashboard.html', context)




def get_user_expenses():
    hotel_reservations = HotelReservation.objects.values('user').annotate(total_price=Sum('total_price'))
    travel_reservations = TravelReservation.objects.values('user').annotate(total_price=Sum('total_price'))

    print(hotel_reservations)
    print(travel_reservations)

    user_expenses = {}
    for reservation in hotel_reservations:
        user_expenses[reservation['user']] = user_expenses.get(reservation['user'], 0) + reservation['total_price']
    for reservation in travel_reservations:
        user_expenses[reservation['user']] = user_expenses.get(reservation['user'], 0) + reservation['total_price']

    print(user_expenses)

    return user_expenses

def all_reservations(request):
    flight_reservations = TravelReservation.objects.all()
    hotel_reservations = HotelReservation.objects.all()
    package_reservations = PackageReservation.objects.all()

    return render(request, 'travely_auth/all_reservations.html', {
        'flight_reservations': flight_reservations,
        'hotel_reservations': hotel_reservations,
        'package_reservations': package_reservations,
    })


########################