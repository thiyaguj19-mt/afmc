from django.contrib import admin
from .models import *

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'type', 'email', 'status')
    list_filter = ('type', 'status')
admin.site.register(Provider, ProviderAdmin)

class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'assigned_to', 'status')
    list_filter = ('status', 'assigned_to')
admin.site.register(Activities, ActivitiesAdmin)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'status')
    list_filter = ('status', 'first_name')
admin.site.register(Volunteer, VolunteerAdmin)

class CredentialingAdmin(admin.ModelAdmin):
    list_display = ('type', 'year', 'status', 'license_duedate', 'provider')
    list_filter = ('type', 'status', 'license_duedate', 'year', 'provider')
admin.site.register(Credentialing, CredentialingAdmin)
