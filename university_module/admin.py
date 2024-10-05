# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(UniversityList)
class UniversityListAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'campuslist')
    search_fields = ('university_name', 'campuslist')
    list_filter = ('campuslist',)


@admin.register(CollageList)
class CollageListAdmin(admin.ModelAdmin):
    list_display = ('collage_name', 'university_list')
    search_fields = ('collage_name', 'university_list')
    list_filter = ('university_list',)


@admin.register(ProgrammeList)
class ProgrammeListAdmin(admin.ModelAdmin):
    list_display = ('programme_name', 'collagelist', 'universitylist')
    search_fields = ('programme_name', 'collagelist', 'universitylist')
    list_filter = ('collagelist',)
