# Generated by Django 4.1.3 on 2022-11-08 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sneaker_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='price',
            field=models.IntegerField(verbose_name='Purchase Price'),
        ),
    ]
