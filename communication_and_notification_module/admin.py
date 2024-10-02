from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(CommunicationLog)
class CommunicationLogAdmin(admin.ModelAdmin):
    list_display = ('StudentProfile', 'method', 'date')
    search_fields = ('student__first_name', 'student__last_name', 'method')