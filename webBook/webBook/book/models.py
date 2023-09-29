from django.db import models

# Modelo para estudios de animaciones
class Editorial(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"
        ordering = ['-created']

    def __str__(self):
        return self.name

# Modelo para categorías de animaciones
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name

# Modelo para tipo de animaciones
class Type(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ['-created']

    def __str__(self):
        return self.name

# Modelo para animaciones
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    description = models.TextField(verbose_name="Descripción")
    year = models.IntegerField(verbose_name="Año")
    image = models.ImageField(verbose_name="imagen", upload_to="anime") #estos quedan guardados en media/anime
    type = models.ForeignKey(Type, verbose_name="Tipo", on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name="Categorías")
    editorials = models.ManyToManyField(Editorial, verbose_name="Editoriales")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['-created']

    def __str__(self):
        return self.title
