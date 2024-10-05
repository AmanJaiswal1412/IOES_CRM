from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'created_date')


@admin.register(StudentPermanentAddress)
class StudentPermanentAddressAdmin(admin.ModelAdmin):
        list_display = ('student', 'state', 'city', 'postal_code', 'created_date')
    # search_fields = ('first_name', 'last_name', 'email')


@admin.register(StudentTempAddress)
class StudentTempAddressAdmin(admin.ModelAdmin):
        list_display = ('student', 'state', 'city', 'postal_code', 'created_date')