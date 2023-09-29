from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    image = models.ImageField(verbose_name='imagen', upload_to="projects")
    link = models.URLField(verbose_name='Dirección web', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha_creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha_actualización')

    class Meta():
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
