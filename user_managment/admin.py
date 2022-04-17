from django.contrib import admin

from user_managment.models import Doctor
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class DoctorAdmin(UserAdmin):
    list_display=('username','address','clock_in','phone_number','is_admin','is_staff')
    search_fields=('username',)
    readonly_fields=('phone_number','clock_in')

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Doctor,DoctorAdmin)
