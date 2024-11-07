from django.db import models
from .enums import Color, Parity, Range

# Create your models here.
COLOR_CHOICES = [(color.value, color.name) for color in Color]
PARITY_CHOICES = [(par.value, par.name) for par in Parity]
RANGE_CHOICES = [(ranges.value, ranges.name) for ranges in Range]


class BlackRedEntry(models.Model):

    color = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=Color.OTHER.value
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    marked = models.BooleanField(default=False)  # For 'X' marker

class OddEvenEntry(models.Model):

    parity = models.CharField(
        max_length=2,
        choices=PARITY_CHOICES,
        default=Parity.ERR.value
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    marked = models.BooleanField(default=False)  # For 'X' marker

class HighLowEntry(models.Model):

    range_value = models.CharField(
        max_length=2,
        choices=RANGE_CHOICES,
        default=Range.ERR.value
    )

    marked = models.BooleanField(default=False)

class NumberStatistics(models.Model):

    # Store all records
    timestamp = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField()
    color = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=Color.OTHER.value
    )

    parity = models.CharField(
        max_length=2,
        choices=PARITY_CHOICES,
        default=Parity.ERR.value
    )

    range_value = models.CharField(
        max_length=2,
        choices=RANGE_CHOICES,
        default=Range.ERR.value
    )

