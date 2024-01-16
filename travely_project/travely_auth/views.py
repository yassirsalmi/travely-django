from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .forms import UserProfileForm, CustomPasswordChangeForm
from django.views import View
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# from django.contrib.auth.models import CustomUser


#views form account management



class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('user_profile')











# redirect views 


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

# def admin_dashboard(request):
#     # Get all users or perform other admin-related tasks
#     users = CustomUser.objects.all()
#     context = {'users': users}
#     return render(request, 'admin_dashboard.html', context)



######################

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(is_admin, login_url='/login/')
def admin_dashboard(request):
    users = CustomUser.objects.filter(is_admin=True) | CustomUser.objects.filter(is_client=True)
    # Exclude the superuser
    users = users.exclude(is_superuser=True)

    context = {'users': users}
    return render(request, 'admin/admin_dashboard.html', context)

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

#sign up and sign in views

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_visitor:
                user.is_visitor = False
                user.is_client = True
                user.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log the user in after signup
#             return redirect('home')  # Redirect to the home page or wherever you want
#     else:
#         form = UserCreationForm()

#     return render(request, 'registration/signup.html', {'form': form})
