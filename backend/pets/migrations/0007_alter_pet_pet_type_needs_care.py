# Generated by Django 4.1.5 on 2023-02-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_remove_pet_pet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_type_needs_care',
            field=models.CharField(default='OTHER', max_length=50),
        ),
    ]