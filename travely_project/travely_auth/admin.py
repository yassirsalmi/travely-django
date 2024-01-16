# from django.contrib import admin
# from  travely_auth.models import CustomUser

# # Register your models here.
# admin.site.register(CustomUser),


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('username', 'email', 'first_name', 'last_name',)

admin.site.register(CustomUser, CustomUserAdmin)