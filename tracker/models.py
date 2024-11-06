from django.db import models
from .enums import Color, Parity, Range
    
    
# Create your models here.

class BlackRedEntry(models.Model):
    
    COLOR_CHOICES = [(color.value, color.name) for color in Color]
    
    color = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=Color.OTHER.value
    )
     
    timestamp = models.DateTimeField(auto_now_add=True)
    marked = models.BooleanField(default=False)  # For 'X' marker
    
class OddEvenEntry(models.Model):
    PARITY_CHOICES = [(par.value, par.name) for par in Parity]
    
    parity = models.IntegerField(
        max_length=2,
        choices=PARITY_CHOICES,
        default=Parity.ERR.value
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    marked = models.BooleanField(default=False)  # For 'X' marker  
    

class HighLowEntry(models.Model):
    
    RANGE_CHOICES = [(ranges.value, ranges.name) for ranges in Parity]
    
    range_value = models.IntegerField(
        max_length=2,
        choices=RANGE_CHOICES,
        default=Range.ERR.value
    )
    
    timestamp = models.DateTimeField(auto_now_add=True)
    marked = models.BooleanField(default=False) 