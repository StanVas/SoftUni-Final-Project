from django.core.validators import MinLengthValidator
from django.db import models

from tattoo_web.accounts.models import UserProfile
from tattoo_web.core.utils import validate_file_size


class ArtistPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    photo = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        ),
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
    )

    date_of_publication = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    class Meta:
        ordering = ['-date_of_publication']


class UserPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 5
    MAX_DESCRIPTION_LENGTH = 300

    photo = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        ),
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
    )

    date_of_publication = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ['-date_of_publication']
