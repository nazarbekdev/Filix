# Generated by Django 5.0.3 on 2024-03-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouses',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
