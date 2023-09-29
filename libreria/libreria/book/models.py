from django.db import models
from author.models import Author

# Modelo para editoriales de libros
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

# Modelo para categorías de libros
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

# Modelo para tipo de libros
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

# Modelo para Libros
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    description = models.TextField(verbose_name="Descripción")
    year = models.IntegerField(verbose_name="Año")
    image = models.ImageField(verbose_name="imagen", upload_to="libros") #estos quedan guardados en media/anime
    type = models.ForeignKey(Type, verbose_name="Tipo", on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, verbose_name="Autor", on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name="Categorías")
    editorial = models.ForeignKey(Editorial, verbose_name="Editorial", on_delete=models.SET_NULL, null=True, blank=True)
    number_downloads = models.IntegerField(verbose_name="Número de descagas", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['-created']

    def __str__(self):
        return self.title + "-" + self.subtitle


# modelo para tipos de archivos de libros
class TypeFile(models.Model):
    # file
    name = models.CharField(max_length=200, verbose_name="Nombre")

    class Meta:
        verbose_name = "Tipo de archivo"
        verbose_name_plural = "tipos de archivos"
        ordering = ['-name']

    def __str__(self):
        return self.name

# modelo para el lenguaje de un libro
class Language(models.Model):
    # file
    name = models.CharField(max_length=200, verbose_name="Lenguaje")

    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"
        ordering = ['-name']

    def __str__(self):
        return self.name

# modelo para los archivos de un libro
class File(models.Model):
    file = models.FileField(upload_to="book_files", verbose_name="Archivo")
    typeFile = models.ForeignKey(TypeFile, verbose_name="Tipo de archivo", on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, verbose_name="Lenguaje", on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, verbose_name="Libro", on_delete=models.CASCADE)
    number_pages = models.IntegerField(verbose_name="Número de páginas")
    number_downloads = models.IntegerField(verbose_name="Número de descagas")

    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"

    def __str__(self):
        return self.book.title