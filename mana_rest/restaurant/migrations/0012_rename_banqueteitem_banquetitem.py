# Generated by Django 4.2.15 on 2024-09-09 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_banquet_food_category_food_is_available_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BanqueteItem',
            new_name='BanquetItem',
        ),
    ]