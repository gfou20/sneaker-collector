# Generated by Django 4.1.3 on 2022-11-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]