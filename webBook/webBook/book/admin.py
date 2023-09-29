from django.contrib import admin
from .models import Book, Category, Editorial, Type

# Register your models here.
class EditorialAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')

class TypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'year', 'type', 'anime_categories', 'anime_editorials')
    ordering = ('title', 'type')
    list_filter = ('title', 'type', 'categories', 'editorials')
    search_fields = ('title', 'categories__name', 'editorials__name')

    def anime_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    def anime_editorials(self, obj):
        return ", ".join([c.name for c in obj.editorials.all().order_by("name")])

    anime_categories.short_description = "Categorías"
    anime_editorials.short_description = "Editoriales"

admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Book, BookAdmin)
