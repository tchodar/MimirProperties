from django.contrib.gis.db import models as gis_models
from django.db import models

from .base import EntityBaseModel


class AddressModel(EntityBaseModel, models.Model):

    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, null=True)
    line3 = models.CharField(max_length=255, null=True)
    coordinates = gis_models.PointField()