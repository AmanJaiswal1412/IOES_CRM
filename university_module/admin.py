# Register your models here.
from django.contrib import admin
from .models import UniversityList


@admin.register(UniversityList)
class UniversityListAdmin(admin.ModelAdmin):
    list_display = ('name', 'countrylist')
    search_fields = ('name', 'countrylist')
    list_filter = ('countrylist',)
