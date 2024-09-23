# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AppUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = UserCreationForm.Meta.fields + (
            "first_name", 
            "last_name", 
            "phone_number", 
            "department",   
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser
        fields = UserChangeForm.Meta.fields 
