# Generated by Django 4.1.5 on 2023-01-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsitters', '0005_alter_petsitter_photo_petsitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsitter',
            name='photo_petsitter',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]