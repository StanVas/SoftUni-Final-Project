# Generated by Django 4.2.3 on 2023-08-08 10:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_extra_image_alter_article_main_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sub_title',
            field=models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
