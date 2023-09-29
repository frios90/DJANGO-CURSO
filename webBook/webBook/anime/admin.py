from django.contrib import admin
from .models import Anime, Category, Studio, Type

# Register your models here.
class StudioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')

class TypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')

class AnimeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'year', 'type', 'anime_categories', 'anime_studios')
    ordering = ('title', 'type')
    list_filter = ('title', 'type', 'categories', 'studios')
    search_fields = ('title', 'categories__name', 'studios__name')

    def anime_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    def anime_studios(self, obj):
        return ", ".join([c.name for c in obj.studios.all().order_by("name")])

    anime_categories.short_description = "Categorías"
    anime_studios.short_description = "Estudios"

admin.site.register(Studio, StudioAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Anime, AnimeAdmin)
