from django.contrib import admin
from .models import Book, Category, Editorial, Type, TypeFile, Language, File

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
    list_display = ('title', 'subtitle', 'year', 'type', 'editorial', 'book_categories')
    ordering = ('title', 'type')
    list_filter = ('title', 'type', 'categories', 'editorial')
    search_fields = ('title', 'editorial', 'categories__name')

    def book_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    book_categories.short_description = "Categorías"

class TypeFileAdmin(admin.ModelAdmin):
    list_display = ('name',)

class LanguajeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FileAdmin(admin.ModelAdmin):
    list_display = ('book_parent', 'number_downloads')
    list_filter = ('book',)

    def book_parent(self, obj):
        return obj.book.title

    book_parent.short_description = "libro"

admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(TypeFile, TypeFileAdmin)
admin.site.register(Language, LanguajeAdmin)
admin.site.register(File, FileAdmin)
