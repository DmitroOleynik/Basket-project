# Generated by Django 5.2.4 on 2025-07-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_bookproduct_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_born',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_death',
            field=models.DateField(default=None, null=True),
        ),
    ]
