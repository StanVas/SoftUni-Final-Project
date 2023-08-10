from django.db import models

from tattoo_web.accounts.models import UserProfile
from tattoo_web.photos.models import ArtistPhoto, UserPhoto


class ArtistPhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    photo = models.ForeignKey(
        ArtistPhoto,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    class Meta:
        ordering = ['-date_time_of_publication']


class UserPhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    photo = models.ForeignKey(
        UserPhoto,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    class Meta:
        ordering = ['-date_time_of_publication']

# class PhotoLike(models.Model):
#     pass
