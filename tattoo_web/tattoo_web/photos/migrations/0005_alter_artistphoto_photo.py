# Generated by Django 4.2.3 on 2023-08-05 15:36

from django.db import migrations, models
import tattoo_web.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_userphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistphoto',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[tattoo_web.core.utils.validate_file_size]),
        ),
    ]
