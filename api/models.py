from django.contrib.gis.db import models  # for adding geospatial fields


class CovidHospbeds(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.PointField()
    factly_nam = models.CharField(max_length=254, default="None")
    totalbeds = models.BigIntegerField(blank=False, null=False, default=0)
    ncv = models.BigIntegerField(blank=True, null=True)
    nco = models.BigIntegerField(blank=True, null=True)
    nci = models.BigIntegerField(blank=True, null=True)
    cvv = models.BigIntegerField(blank=True, null=True)
    cov = models.BigIntegerField(blank=True, null=True)
    civ = models.BigIntegerField(blank=True, null=True)
    cvr = models.BigIntegerField(blank=True, null=True)
    cor = models.BigIntegerField(blank=True, null=True)
    cir = models.BigIntegerField(blank=True, null=True)
    cvo = models.BigIntegerField(blank=True, null=True)
    coo = models.BigIntegerField(blank=True, null=True)
    cio = models.BigIntegerField(blank=True, null=True)
