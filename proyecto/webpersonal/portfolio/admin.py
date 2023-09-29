from django.contrib import admin
from .models import Project


class ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProyectAdmin)
