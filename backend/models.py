from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Beacons(models.Model):
    beacon_1 = models.IntegerField(default=130, blank=False, null=False)
    beacon_2 = models.IntegerField(default=130, blank=False, null=False)
    beacon_3 = models.IntegerField(default=130, blank=False, null=False)
    beacon_4 = models.IntegerField(default=130, blank=False, null=False)
    beacon_5 = models.IntegerField(default=130, blank=False, null=False)
    beacon_6 = models.IntegerField(default=130, blank=False, null=False)
    beacon_7 = models.IntegerField(default=130, blank=False, null=False)
    beacon_8 = models.IntegerField(default=130, blank=False, null=False)

    def __str__(self):
      return str(self.id)
    