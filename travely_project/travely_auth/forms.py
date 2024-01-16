from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    profile_picture = forms.ImageField(required=False, label='Profile Picture')

    class Meta:
        model = CustomUser
        fields = ["profile_picture","username", "email","first_name","last_name", "password1", "password2"]


class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Exclude the password field
        self.fields.pop('password')

    # Add 'form-control' class to widgets
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'




class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )