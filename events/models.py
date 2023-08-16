from django.core.validators import MinLengthValidator
from django.db import models

from events.validators import validate_date


# Create your models here.
class EventModel(models.Model):
    CHOICES = (
        ('Sports', "Sports"),
        ('Festivals', "Festivals"),
        ('Conferences', "Conferences"),
        ('Performing Art', "Performing Art"),
        ('Concerts', "Concerts"),
        ('Theme Party', "Theme Party"),
        ('Other', "Other"),
    )

    event_name = models.CharField(
        max_length=30,
        verbose_name='Event Name',
        validators=[
            MinLengthValidator(2)
        ]
    )
    category = models.CharField(
        max_length=14,
        choices=CHOICES,
        verbose_name='Category',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description'
    )
    date = models.DateTimeField(
        verbose_name='Date',
        validators=[
            validate_date,
        ]
    )
    event_image = models.URLField(
        verbose_name='Event Image',
    )

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
