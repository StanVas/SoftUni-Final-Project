from django.core.validators import MinLengthValidator
from django.db import models

from tattoo_web.core.model_mixins import StrFromFieldsMixin
from tattoo_web.photos.validators import validate_file_size


# class ArtistPhoto(StrFromFieldsMixin, models.Model):
class ArtistPhoto(models.Model):
    str_fields = (id,)

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    # TODO: change this to ImageField / make it blank=False
    photo = models.URLField(
        # upload_to='',
        null=False,
        blank=True,
        # validators=(
        #     validate_file_size,
        # ),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )


# class UserPhoto(models.Model):
#     pass
