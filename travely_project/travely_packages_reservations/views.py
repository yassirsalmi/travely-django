from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PackageReservation
from .forms import PackageReservationForm


def is_admin(user):
    return user.is_authenticated and user.is_admin

@login_required
@user_passes_test(is_admin, login_url='/login/')
def add_package(request):
    if request.method == 'POST':
        form = PackageReservationForm(request.POST, request.FILES)
        if form.is_valid():
            package_reservation = form.save(commit=False)
            package_reservation.user = request.user
            package_reservation.save()
            return redirect('travely_auth:admin_dashboard')  
    else:
        form = PackageReservationForm()
    return render(request, 'travely_packages_reservations/add_package.html', {'form': form})


def all_packages(request):
    packages = PackageReservation.objects.all() 
    return render(request, 'travely_auth/packages.html', {'packages': packages})


def package_details(request, pk):
    package = get_object_or_404(PackageReservation, pk=pk)
    return render(request, 'travely_packages_reservations/package_details.html', {'package': package})


@login_required
@user_passes_test(is_admin, login_url='/login/')
def modify_package(request, pk):
    package = get_object_or_404(PackageReservation, pk=pk)
    if request.method == 'POST':
        form = PackageReservationForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect('travely_auth:admin_dashboard')
    else:
        form = PackageReservationForm(instance=package)
    return render(request, 'travely_packages_reservations/modify_package.html', {'form': form, 'package': package})

@login_required
@user_passes_test(is_admin, login_url='/login/')
def delete_package(request, pk):
    package = get_object_or_404(PackageReservation, pk=pk)
    if request.method == 'POST':
        package.delete()
        return redirect('travely_auth:admin_dashboard')
    return render(request, 'travely_packages_reservations/delete_package.html', {'package': package})


@login_required
@user_passes_test(is_admin, login_url='/login/')
def all_packages_admin(request):
    packages = PackageReservation.objects.all() 
    return render(request, 'travely_packages_reservations/all_packages.html', {'packages': packages})


#######################################
from django.shortcuts import render, get_object_or_404
from .models import PackageReservation, ReservationProcess
from .forms import ReservationProcessForm
@login_required
def reserve_package(request, pk):
    package = get_object_or_404(PackageReservation, pk=pk)
    if request.method == 'POST':
        form = ReservationProcessForm(request.POST)
        if form.is_valid():
            reservation_process = form.save(commit=False)
            reservation_process.user = request.user
            reservation_process.package_reservation = package
            reservation_process.save()
            return redirect('travely_auth:home')
    else:
        form = ReservationProcessForm()
    return render(request, 'travely_packages_reservations/package_reservations.html', {'package': package, 'form': form})