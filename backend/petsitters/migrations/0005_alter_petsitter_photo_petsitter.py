# Generated by Django 4.1.5 on 2023-01-30 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsitters', '0004_petsitter_photo_petsitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsitter',
            name='photo_petsitter',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]