# Generated by Django 3.1 on 2020-08-05 03:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_app', '0002_auto_20200804_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='city',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='email',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='phone',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='site',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='state',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='street',
            field=models.TextField(default=''),
        ),
    ]