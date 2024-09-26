from django.contrib import admin
from .models import AppUser

# Register your models here.
@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'department']
    list_per_page = 10
    search_fields = ["email",'first_name__istartswith', 'last_name__istartswith']
    # list_select_related = ['degree_program'] A field ambayo ni foreign key iweke kwenye select related
    # list_editable = ['subscribed']