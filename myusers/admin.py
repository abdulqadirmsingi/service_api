from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import AppUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = AppUser
    list_display = ["username", "phone_number", "department"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone_number", "department")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("phone_number", "department")}),)

admin.site.register(AppUser, CustomUserAdmin)

