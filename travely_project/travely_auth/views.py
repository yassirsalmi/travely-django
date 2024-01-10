from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# redirect functions 

def about_page_view(request):
    return render(request, 'travely_auth/about_page.html')  

# this line is used to restrict acces to a page if the user is not logged in 
# @login_required(login_url="/login")
def services_page_view(request):
    return render(request, 'travely_auth/services_page.html')  




# 


def home(request):
    return render(request, 'travely_auth/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
