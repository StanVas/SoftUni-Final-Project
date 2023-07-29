import re

from django.core.exceptions import ValidationError


def validate_only_alphabetical(value):
    if not re.match(r'^[a-zA-Z]+$', value):
        raise ValidationError('Must contain only alphabetical letters!')
