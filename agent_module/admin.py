# Register your models here.
from django.contrib import admin
from .models import Agent
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'region', 'commission_rate')
    search_fields = ('name', 'region')
    list_filter = ('region',)


class AgentInline(admin.StackedInline):
    model = Agent
    can_delete = False
    verbose_name_plural = 'Agent Profile'


class CustomUserAdmin(UserAdmin):
    inlines = (AgentInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
