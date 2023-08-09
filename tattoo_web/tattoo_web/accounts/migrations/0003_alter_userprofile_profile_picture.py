# Generated by Django 4.2.3 on 2023-08-07 15:07

from django.db import migrations, models
import tattoo_web.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[tattoo_web.core.utils.validate_file_size]),
        ),
    ]