from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'last_name','created', 'updated')
    ordering = ('name', 'last_name',)
    search_fields = ('name', 'last_name',)

admin.site.register(Author, AuthorAdmin)
