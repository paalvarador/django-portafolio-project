# Generated by Django 4.2.13 on 2024-06-12 17:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_profile_cv_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='project_images'),
        ),
    ]
