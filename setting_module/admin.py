from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(LeadSource)
class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ('source_name', 'created_date', 'updated_date')
    search_fields = ['source_name']


@admin.register(DocumentList)
class DocumentListAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'created_date', 'updated_date')
    search_fields = ['document_name']


@admin.register(CountryList)
class CountryListAdmin(admin.ModelAdmin):
    list_display = ('country_list', 'created_date', 'updated_date')
    search_fields = ['country_list']


@admin.register(CityList)
class CityListAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'country_list', 'created_date', 'updated_date')
    search_fields = ['country_list']


@admin.register(UniversityCampus)
class UniversityCampusAdmin(admin.ModelAdmin):
    list_display = ('campus_name', 'created_date', 'updated_date')
    search_fields = ['campus_city']


@admin.register(IntakeList)
class IntakeListAdmin(admin.ModelAdmin):
    list_display = ('intake_year', 'created_date', 'updated_date')