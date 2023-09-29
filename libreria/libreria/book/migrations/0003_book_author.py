# Generated by Django 4.2.2 on 2023-06-27 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_description'),
        ('book', '0002_remove_book_editorials_book_editorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='author.author', verbose_name='Autor'),
        ),
    ]