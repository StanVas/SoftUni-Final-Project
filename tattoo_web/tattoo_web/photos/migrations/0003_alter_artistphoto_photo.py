# Generated by Django 4.2.3 on 2023-07-31 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_photo_artistphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistphoto',
            name='photo',
            field=models.URLField(blank=True),
        ),
    ]
