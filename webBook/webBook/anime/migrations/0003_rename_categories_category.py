# Generated by Django 4.2.2 on 2023-06-27 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_categories_alter_anime_options_anime_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
