from django.core.exceptions import ValidationError


def only_alpha_characters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("The name should contain only letters!")


def contains_digit_validator(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError("The password must contain at least 1 digit!")
