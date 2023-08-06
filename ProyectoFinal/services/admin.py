from django.contrib import admin
from .models import Service

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServicesAdmin)
