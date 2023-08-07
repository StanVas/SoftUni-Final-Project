from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.templatetags.static import static

from tattoo_web.accounts.validators import validate_only_alphabetical
from tattoo_web.core.utils import validate_file_size


class UserProfile(AbstractUser):
    USER_NAME_MAX_LENGTH = 30
    USER_NAME_MIN_LENGTH = 3
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2

    username = models.CharField(
        unique=True,
        max_length=USER_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USER_NAME_MIN_LENGTH),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_alphabetical,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_alphabetical,
        ),
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        ),
        # default=static('img/person.png'),
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
