# Generated by Django 4.1.3 on 2022-11-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_location_alter_release_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='locations',
            field=models.ManyToManyField(to='main_app.location'),
        ),
    ]