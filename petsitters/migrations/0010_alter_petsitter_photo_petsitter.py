# Generated by Django 4.1.5 on 2023-02-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsitters', '0009_alter_petsitter_photo_petsitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsitter',
            name='photo_petsitter',
            field=models.ImageField(default='https://pet-care-exchange-static.s3.us-west-2.amazonaws.com/blank-profile-picture.jpg', upload_to=''),
        ),
    ]
