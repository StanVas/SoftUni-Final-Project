# Generated by Django 4.2.3 on 2023-07-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_main_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_text',
            field=models.TextField(),
        ),
    ]
