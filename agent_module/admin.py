# Register your models here.
from django.contrib import admin
from .models import Agent, BussinessInfo
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'commission_rate')
    search_fields = ('name', 'location')
    list_filter = ('location',)


@admin.register(BussinessInfo)
class BussinessInfoAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'business_phone', 'business_location')
    search_fields = ('business_name', 'business_phone',)
    list_filter = ('business_location',)


class AgentInline(admin.StackedInline):
    model = Agent
    can_delete = False
    verbose_name_plural = 'Agent Profile'


class CustomUserAdmin(UserAdmin):
    inlines = (AgentInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
