# Generated by Django 4.2.13 on 2024-06-12 05:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_profile_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='cv'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='profile_picture'),
        ),
    ]
