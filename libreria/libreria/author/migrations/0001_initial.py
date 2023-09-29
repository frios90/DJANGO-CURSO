# Generated by Django 4.2.2 on 2023-06-27 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=200, verbose_name='Apellido')),
                ('born_date', models.DateField(blank=True, max_length=200, null=True, verbose_name='Fecha nacimiento')),
                ('description', models.TextField(verbose_name='Reseña')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['-created'],
            },
        ),
    ]
