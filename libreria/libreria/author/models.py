from django.db import models

# Modelo para autores
class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    last_name = models.CharField(max_length=200, verbose_name="Apellido")
    born_date = models.DateField(max_length=200, verbose_name="Fecha nacimiento", null=True, blank=True)
    description = models.TextField(verbose_name="Reseña", null=True, blank=True)
    image = models.ImageField(verbose_name="imagen", upload_to="author", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['-created']

    def __str__(self):
        return f"{self.last_name}, {self.name}"