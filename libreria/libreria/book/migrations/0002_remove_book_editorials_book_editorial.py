# Generated by Django 4.2.2 on 2023-06-27 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='editorials',
        ),
        migrations.AddField(
            model_name='book',
            name='editorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.editorial', verbose_name='Editorial'),
        ),
    ]
