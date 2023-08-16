from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import only_alpha_characters_validator, contains_digit_validator


# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='First Name',
        validators=[
            only_alpha_characters_validator,
        ])
    last_name = models.CharField(
        max_length=30,
        verbose_name='Last Name',
        validators=[
            MinLengthValidator(4)
        ]
    )
    email = models.EmailField(
        max_length=45,
        verbose_name='Email',
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture',
    )
    password = models.CharField(
        max_length=20,
        verbose_name='Password',
        validators=[
            MinLengthValidator(5),
            contains_digit_validator,
        ]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
