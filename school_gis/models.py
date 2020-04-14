# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class InstMsbvee12Apr2020(models.Model):
    fid_1 = models.AutoField(primary_key=True)
    # the_geom = models.PointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    category = models.CharField(db_column='Category', max_length=254, blank=True, null=True)  # Field name made lowercase.
    specify_if = models.CharField(max_length=254, blank=True, null=True)
    dvet_inst_field = models.CharField(db_column='dvet_inst_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    inst_name = models.CharField(max_length=254, blank=True, null=True)
    inst_type = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=254, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=254, blank=True, null=True)  # Field name made lowercase.
    area_name = models.CharField(max_length=254, blank=True, null=True)
    city_villa = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    taluka = models.CharField(max_length=254, blank=True, null=True)
    pincode = models.BigIntegerField(db_column='Pincode', blank=True, null=True)  # Field name made lowercase.
    photo_of_t = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.inst_name

    class Meta:
        managed = False
        db_table = 'inst_msbvee_12apr2020'

