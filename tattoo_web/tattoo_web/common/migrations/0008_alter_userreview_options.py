# Generated by Django 4.2.3 on 2023-08-16 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_userreview_date_of_publication_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userreview',
            options={'ordering': ['-date_of_publication']},
        ),
    ]
