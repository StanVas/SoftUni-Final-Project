# Generated by Django 4.2.3 on 2023-08-10 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_alter_artistphoto_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artistphoto',
            options={'ordering': ['-date_of_publication']},
        ),
        migrations.AlterModelOptions(
            name='userphoto',
            options={'ordering': ['-date_of_publication']},
        ),
    ]
