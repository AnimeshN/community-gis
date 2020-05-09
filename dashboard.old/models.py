#from django.db import models
from django.contrib.gis.db import models


class ThakkarbappayojanaMokhadaCulvert10(models.Model):
    fid_1 = models.AutoField(primary_key=True)
    the_geom = models.PointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    panchayat_field = models.CharField(db_column='Panchayat_', max_length=254, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    village_na = models.CharField(db_column='Village_Na', max_length=254, blank=True, null=True)  # Field name made lowercase.
    habitation = models.CharField(db_column='Habitation', max_length=254, blank=True, null=True)  # Field name made lowercase.
    budget = models.CharField(db_column='Budget', max_length=254, blank=True, null=True)  # Field name made lowercase.
    sanction_y = models.CharField(db_column='Sanction_y', max_length=254, blank=True, null=True)  # Field name made lowercase.
    work_type = models.CharField(db_column='Work_type', max_length=254, blank=True, null=True)  # Field name made lowercase.
    work_name = models.CharField(db_column='Work_Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    width = models.CharField(db_column='Width', max_length=254, blank=True, null=True)  # Field name made lowercase.
    no_of_pipe = models.CharField(db_column='No_of_Pipe', max_length=254, blank=True, null=True)  # Field name made lowercase.
    final_asse = models.CharField(db_column='Final_Asse', max_length=254, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThakkarBappaYojana_Mokhada_Culvert_1_0'
