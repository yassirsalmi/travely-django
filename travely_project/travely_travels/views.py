from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TravelForm, PromotionForm, CategoryForm
from .models import Travel

@login_required
def add_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.created_by = request.user
            travel.save()
            return redirect('travely_auth:admin_dashboard')
    else:
        form = TravelForm()

    return render(request, 'travely_travels/add_travel.html', {'form': form})

@login_required
def all_travels(request):
    travels = Travel.objects.all()
    return render(request, 'travely_travels/all_travels.html', {'travels': travels})

@login_required
def modify_travel(request, travel_id):
    travel = get_object_or_404(Travel, id=travel_id)

    if request.user != travel.created_by:
        return redirect('access_denied')

    if request.method == 'POST':
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travely_travels:all_travels')
    else:
        form = TravelForm(instance=travel)

    return render(request, 'travely_travels/modify_travel.html', {'form': form, 'travel': travel})

@login_required
def delete_travel(request, travel_id):
    travel = get_object_or_404(Travel, id=travel_id)

    if request.user != travel.created_by:
        return redirect('access_denied')

    travel.delete()
    return redirect('travely_travels:all_travels')

@login_required
def add_promotion(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('travely_auth:admin_dashboard')
    else:
        form = PromotionForm()

    return render(request, 'travely_travels/add_promotion.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('travely_auth:admin_dashboard')
    else:
        form = CategoryForm()

    return render(request, 'travely_travels/add_category.html', {'form': form})

def travel_details(request, travel_id):
    travel = get_object_or_404(Travel, id=travel_id)
    return render(request, 'travely_travels/travel_details.html', {'travel': travel})
