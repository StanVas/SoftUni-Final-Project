from django.core.validators import MinLengthValidator
from django.db import models


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
        null=True,
        blank=True,
    )

    main_image = models.URLField(
        null=True,
        blank=True,
    )

    extra_image = models.URLField(
        null=True,
        blank=True,
    )
