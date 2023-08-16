from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("The date cannot be in the past!")
