# Generated by Django 4.2.15 on 2024-09-26 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_rename_banquete_banquetitem_banquet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketitem',
            name='discount',
        ),
        migrations.AddField(
            model_name='food',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]