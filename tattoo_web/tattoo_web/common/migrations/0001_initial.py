# Generated by Django 4.2.3 on 2023-08-04 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0004_userphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistPhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('date_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.artistphoto')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
