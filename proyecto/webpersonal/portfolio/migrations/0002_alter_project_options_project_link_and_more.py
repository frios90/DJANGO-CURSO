# Generated by Django 4.2.2 on 2023-06-17 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha_creación'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='título'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha_actualización'),
        ),
    ]
