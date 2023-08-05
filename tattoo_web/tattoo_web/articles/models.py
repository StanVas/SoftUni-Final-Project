from django.core.validators import MinLengthValidator
from django.db import models

from tattoo_web.core.utils import validate_file_size


# TODO: Change all null and black
class Article(models.Model):
    TITLE_MAX_LENGTH = 50
    TITLE_MIN_LENGTH = 3
    SUB_TITLE_MAX_LENGTH = 50
    SUB_TITLE_MIN_LENGTH = 3

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=(
            MinLengthValidator(TITLE_MIN_LENGTH),
        ),
        null=False,
        blank=False,
    )

    sub_title = models.CharField(
        max_length=SUB_TITLE_MAX_LENGTH,
        validators=(
            MinLengthValidator(SUB_TITLE_MIN_LENGTH),
        ),
        null=False,
        blank=False,
    )

    main_image = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        ),
        null=False,
        blank=False,
    )

    extra_image = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        ),
        null=False,
        blank=False,
    )

    main_text = models.TextField(
        null=False,
        blank=False,
    )
