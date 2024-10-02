from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('student', 'document_type', 'uploaded_at')
    search_fields = ('student__first_name', 'student__last_name', 'document_type')


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ('student', 'universities', 'status', 'updated_at')
    search_fields = ('student__first_name', 'student__last_name', 'universities__name')
    list_filter = ('status',)
