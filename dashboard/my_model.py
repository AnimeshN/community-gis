# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class HealthInstitutes(models.Model):
    fid_1 = models.AutoField(primary_key=True)
    the_geom = models.PointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    srno = models.BigIntegerField(blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    taluka = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    inst_name = models.CharField(max_length=254, blank=True, null=True)
    inst_type = models.CharField(max_length=254, blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Health_Institutes'


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


class ThakkarbappayojanaMokhadaCulvert100(models.Model):
    fid_2 = models.AutoField(primary_key=True)
    the_geom = models.PointField(blank=True, null=True)
    fid_1 = models.IntegerField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    panchayat_field = models.CharField(db_column='Panchayat_', max_length=254, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    village_na = models.CharField(db_column='Village_Na', max_length=254, blank=True, null=True)  # Field name made lowercase.
    habitation = models.CharField(db_column='Habitation', max_length=254, blank=True, null=True)  # Field name made lowercase.
    budget = models.CharField(db_column='Budget', max_length=254, blank=True, null=True)  # Field name made lowercase.
    sanction_y = models.CharField(db_column='Sanction_y', max_length=254, blank=True, null=True)  # Field name made lowercase.
    work_type = models.CharField(db_column='Work_type', max_length=254, blank=True, null=True)  # Field name made lowercase.
    width = models.CharField(db_column='Width', max_length=254, blank=True, null=True)  # Field name made lowercase.
    no_of_pipe = models.CharField(db_column='No_of_Pipe', max_length=254, blank=True, null=True)  # Field name made lowercase.
    final_asse = models.CharField(db_column='Final_Asse', max_length=254, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThakkarBappaYojana_Mokhada_Culvert_1_00'


class ThakkarbappayojanaMokhadaPublictoilet10(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.PointField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    panchayat_field = models.CharField(db_column='Panchayat_', max_length=254, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    village_na = models.CharField(db_column='Village_Na', max_length=254, blank=True, null=True)  # Field name made lowercase.
    habitation = models.CharField(db_column='Habitation', max_length=254, blank=True, null=True)  # Field name made lowercase.
    budget = models.CharField(db_column='Budget', max_length=254, blank=True, null=True)  # Field name made lowercase.
    sanction_y = models.CharField(db_column='Sanction_y', max_length=254, blank=True, null=True)  # Field name made lowercase.
    no_of_wc = models.CharField(db_column='No_of_WC', max_length=254, blank=True, null=True)  # Field name made lowercase.
    no_of_bath = models.CharField(db_column='No_of_Bath', max_length=254, blank=True, null=True)  # Field name made lowercase.
    water_prov = models.CharField(db_column='Water_Prov', max_length=254, blank=True, null=True)  # Field name made lowercase.
    in_use = models.CharField(db_column='In_use', max_length=254, blank=True, null=True)  # Field name made lowercase.
    final_asse = models.CharField(db_column='Final_Asse', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThakkarBappaYojana_Mokhada_PublicToilet_1.0'


class ThakkarbappayojanaMokhadaSamajmandir10(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.PointField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=254, blank=True, null=True)  # Field name made lowercase.
    panchayat_field = models.CharField(db_column='Panchayat_', max_length=254, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    village_na = models.CharField(db_column='Village_Na', max_length=254, blank=True, null=True)  # Field name made lowercase.
    habitation = models.CharField(db_column='Habitation', max_length=254, blank=True, null=True)  # Field name made lowercase.
    budget = models.CharField(db_column='Budget', max_length=254, blank=True, null=True)  # Field name made lowercase.
    sanction_y = models.CharField(db_column='Sanction_y', max_length=254, blank=True, null=True)  # Field name made lowercase.
    work_type = models.CharField(db_column='Work_type', max_length=254, blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=254, blank=True, null=True)  # Field name made lowercase.
    width = models.CharField(db_column='Width', max_length=254, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=254, blank=True, null=True)  # Field name made lowercase.
    electric_f = models.CharField(db_column='Electric_F', max_length=254, blank=True, null=True)  # Field name made lowercase.
    in_use = models.CharField(db_column='In_use', max_length=254, blank=True, null=True)  # Field name made lowercase.
    sanitary_b = models.CharField(db_column='Sanitary_B', max_length=254, blank=True, null=True)  # Field name made lowercase.
    final_asse = models.CharField(db_column='Final_Asse', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThakkarBappaYojana_Mokhada_SamajMandir_1.0'


class ThakkarbappayojanaMokhadaSmashanbhoomi10(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.PointField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    panchayat_field = models.CharField(db_column='Panchayat_', max_length=254, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    village_na = models.CharField(db_column='Village_Na', max_length=254, blank=True, null=True)  # Field name made lowercase.
    habitation = models.CharField(db_column='Habitation', max_length=254, blank=True, null=True)  # Field name made lowercase.
    budget = models.CharField(db_column='Budget', max_length=254, blank=True, null=True)  # Field name made lowercase.
    sanction_y = models.CharField(db_column='Sanction_y', max_length=254, blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=254, blank=True, null=True)  # Field name made lowercase.
    width = models.CharField(db_column='Width', max_length=254, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=254, blank=True, null=True)  # Field name made lowercase.
    chula_ch = models.CharField(max_length=254, blank=True, null=True)
    final_asse = models.CharField(db_column='Final_Asse', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThakkarBappaYojana_Mokhada_Smashanbhoomi_1.0'


class ThakkarbappayojanaMokhadaWell100(models.Model):
    fid_1 = models.AutoField(primary_key=True)
    the_geom = models.PointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    panchayat_field = models.CharField(db_column='Panchayat_', max_length=254, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    village_na = models.CharField(db_column='Village_Na', max_length=254, blank=True, null=True)  # Field name made lowercase.
    habitation = models.CharField(db_column='Habitation', max_length=254, blank=True, null=True)  # Field name made lowercase.
    budget = models.CharField(db_column='Budget', max_length=254, blank=True, null=True)  # Field name made lowercase.
    sanction_y = models.CharField(db_column='Sanction_y', max_length=254, blank=True, null=True)  # Field name made lowercase.
    work_name = models.CharField(db_column='Work_Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    diameter = models.CharField(db_column='Diameter', max_length=254, blank=True, null=True)  # Field name made lowercase.
    depth = models.CharField(db_column='Depth', max_length=254, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=254, blank=True, null=True)  # Field name made lowercase.
    used_for_d = models.CharField(db_column='Used_for_D', max_length=254, blank=True, null=True)  # Field name made lowercase.
    water_avai = models.CharField(db_column='Water_Avai', max_length=254, blank=True, null=True)  # Field name made lowercase.
    final_asse = models.CharField(db_column='Final_Asse', max_length=254, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThakkarBappaYojana_Mokhada_Well_1_00'


class DPalghar(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    census_201 = models.BigIntegerField(blank=True, null=True)
    district_c = models.CharField(max_length=254, blank=True, null=True)
    district_n = models.CharField(max_length=254, blank=True, null=True)
    taluka_cod = models.CharField(max_length=254, blank=True, null=True)
    ward = models.CharField(max_length=254, blank=True, null=True)
    area_name = models.CharField(max_length=254, blank=True, null=True)
    tru = models.CharField(max_length=254, blank=True, null=True)
    no_hh = models.FloatField(blank=True, null=True)
    tot_p = models.FloatField(blank=True, null=True)
    tot_m = models.FloatField(blank=True, null=True)
    tot_f = models.FloatField(blank=True, null=True)
    p_06 = models.FloatField(blank=True, null=True)
    m_06 = models.FloatField(blank=True, null=True)
    f_06 = models.FloatField(blank=True, null=True)
    p_sc = models.FloatField(blank=True, null=True)
    m_sc = models.FloatField(blank=True, null=True)
    f_sc = models.FloatField(blank=True, null=True)
    p_st = models.FloatField(blank=True, null=True)
    m_st = models.FloatField(blank=True, null=True)
    f_st = models.FloatField(blank=True, null=True)
    p_lit = models.FloatField(blank=True, null=True)
    m_lit = models.FloatField(blank=True, null=True)
    f_lit = models.FloatField(blank=True, null=True)
    p_ill = models.FloatField(blank=True, null=True)
    m_ill = models.FloatField(blank=True, null=True)
    f_ill = models.FloatField(blank=True, null=True)
    tot_work_p = models.FloatField(blank=True, null=True)
    tot_work_m = models.FloatField(blank=True, null=True)
    tot_work_f = models.FloatField(blank=True, null=True)
    mainwork_p = models.FloatField(blank=True, null=True)
    mainwork_m = models.FloatField(blank=True, null=True)
    mainwork_f = models.FloatField(blank=True, null=True)
    main_cl_p = models.FloatField(blank=True, null=True)
    main_cl_m = models.FloatField(blank=True, null=True)
    main_cl_f = models.FloatField(blank=True, null=True)
    main_al_p = models.FloatField(blank=True, null=True)
    main_al_m = models.FloatField(blank=True, null=True)
    main_al_f = models.FloatField(blank=True, null=True)
    main_hh_p = models.FloatField(blank=True, null=True)
    main_hh_m = models.FloatField(blank=True, null=True)
    main_hh_f = models.FloatField(blank=True, null=True)
    main_ot_p = models.FloatField(blank=True, null=True)
    main_ot_m = models.FloatField(blank=True, null=True)
    main_ot_f = models.FloatField(blank=True, null=True)
    margwork_p = models.FloatField(blank=True, null=True)
    margwork_m = models.FloatField(blank=True, null=True)
    margwork_f = models.FloatField(blank=True, null=True)
    marg_cl_p = models.FloatField(blank=True, null=True)
    marg_cl_m = models.FloatField(blank=True, null=True)
    marg_cl_f = models.FloatField(blank=True, null=True)
    marg_al_p = models.FloatField(blank=True, null=True)
    marg_al_m = models.FloatField(blank=True, null=True)
    marg_al_f = models.FloatField(blank=True, null=True)
    marg_hh_p = models.FloatField(blank=True, null=True)
    marg_hh_m = models.FloatField(blank=True, null=True)
    marg_hh_f = models.FloatField(blank=True, null=True)
    marg_ot_p = models.FloatField(blank=True, null=True)
    marg_ot_m = models.FloatField(blank=True, null=True)
    marg_ot_f = models.FloatField(blank=True, null=True)
    margwork_3 = models.FloatField(blank=True, null=True)
    margwork_1 = models.FloatField(blank=True, null=True)
    margwork_2 = models.FloatField(blank=True, null=True)
    marg_cl_3_field = models.FloatField(db_column='marg_cl_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_cl_1 = models.FloatField(db_column='marg_cl__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_cl_2 = models.FloatField(db_column='marg_cl__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_3_field = models.FloatField(db_column='marg_al_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_al_1 = models.FloatField(db_column='marg_al__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_2 = models.FloatField(db_column='marg_al__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_3_field = models.FloatField(db_column='marg_hh_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_hh_1 = models.FloatField(db_column='marg_hh__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_2 = models.FloatField(db_column='marg_hh__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_3_field = models.FloatField(db_column='marg_ot_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_ot_1 = models.FloatField(db_column='marg_ot__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_2 = models.FloatField(db_column='marg_ot__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    margwork_0 = models.FloatField(blank=True, null=True)
    margwork_4 = models.FloatField(blank=True, null=True)
    margwork_5 = models.FloatField(blank=True, null=True)
    marg_cl_0_field = models.FloatField(db_column='marg_cl_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_cl_3 = models.FloatField(db_column='marg_cl__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_cl_4 = models.FloatField(db_column='marg_cl__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_0_field = models.FloatField(db_column='marg_al_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_al_3 = models.FloatField(db_column='marg_al__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_4 = models.FloatField(db_column='marg_al__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_0_field = models.FloatField(db_column='marg_hh_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_hh_3 = models.FloatField(db_column='marg_hh__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_4 = models.FloatField(db_column='marg_hh__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_0_field = models.FloatField(db_column='marg_ot_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_ot_3 = models.FloatField(db_column='marg_ot__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    non_work_p = models.FloatField(blank=True, null=True)
    non_work_m = models.FloatField(blank=True, null=True)
    non_work_f = models.FloatField(blank=True, null=True)
    taluka_nam = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_palghar'


class DPalghar0(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    census_201 = models.BigIntegerField(blank=True, null=True)
    district_c = models.CharField(max_length=254, blank=True, null=True)
    district_n = models.CharField(max_length=254, blank=True, null=True)
    taluka_cod = models.CharField(max_length=254, blank=True, null=True)
    ward = models.CharField(max_length=254, blank=True, null=True)
    area_name = models.CharField(max_length=254, blank=True, null=True)
    tru = models.CharField(max_length=254, blank=True, null=True)
    no_hh = models.FloatField(blank=True, null=True)
    tot_p = models.FloatField(blank=True, null=True)
    tot_m = models.FloatField(blank=True, null=True)
    tot_f = models.FloatField(blank=True, null=True)
    p_06 = models.FloatField(blank=True, null=True)
    m_06 = models.FloatField(blank=True, null=True)
    f_06 = models.FloatField(blank=True, null=True)
    p_sc = models.FloatField(blank=True, null=True)
    m_sc = models.FloatField(blank=True, null=True)
    f_sc = models.FloatField(blank=True, null=True)
    p_st = models.FloatField(blank=True, null=True)
    m_st = models.FloatField(blank=True, null=True)
    f_st = models.FloatField(blank=True, null=True)
    p_lit = models.FloatField(blank=True, null=True)
    m_lit = models.FloatField(blank=True, null=True)
    f_lit = models.FloatField(blank=True, null=True)
    p_ill = models.FloatField(blank=True, null=True)
    m_ill = models.FloatField(blank=True, null=True)
    f_ill = models.FloatField(blank=True, null=True)
    tot_work_p = models.FloatField(blank=True, null=True)
    tot_work_m = models.FloatField(blank=True, null=True)
    tot_work_f = models.FloatField(blank=True, null=True)
    mainwork_p = models.FloatField(blank=True, null=True)
    mainwork_m = models.FloatField(blank=True, null=True)
    mainwork_f = models.FloatField(blank=True, null=True)
    main_cl_p = models.FloatField(blank=True, null=True)
    main_cl_m = models.FloatField(blank=True, null=True)
    main_cl_f = models.FloatField(blank=True, null=True)
    main_al_p = models.FloatField(blank=True, null=True)
    main_al_m = models.FloatField(blank=True, null=True)
    main_al_f = models.FloatField(blank=True, null=True)
    main_hh_p = models.FloatField(blank=True, null=True)
    main_hh_m = models.FloatField(blank=True, null=True)
    main_hh_f = models.FloatField(blank=True, null=True)
    main_ot_p = models.FloatField(blank=True, null=True)
    main_ot_m = models.FloatField(blank=True, null=True)
    main_ot_f = models.FloatField(blank=True, null=True)
    margwork_p = models.FloatField(blank=True, null=True)
    margwork_m = models.FloatField(blank=True, null=True)
    margwork_f = models.FloatField(blank=True, null=True)
    marg_cl_p = models.FloatField(blank=True, null=True)
    marg_cl_m = models.FloatField(blank=True, null=True)
    marg_cl_f = models.FloatField(blank=True, null=True)
    marg_al_p = models.FloatField(blank=True, null=True)
    marg_al_m = models.FloatField(blank=True, null=True)
    marg_al_f = models.FloatField(blank=True, null=True)
    marg_hh_p = models.FloatField(blank=True, null=True)
    marg_hh_m = models.FloatField(blank=True, null=True)
    marg_hh_f = models.FloatField(blank=True, null=True)
    marg_ot_p = models.FloatField(blank=True, null=True)
    marg_ot_m = models.FloatField(blank=True, null=True)
    marg_ot_f = models.FloatField(blank=True, null=True)
    margwork_3 = models.FloatField(blank=True, null=True)
    margwork_1 = models.FloatField(blank=True, null=True)
    margwork_2 = models.FloatField(blank=True, null=True)
    marg_cl_3_field = models.FloatField(db_column='marg_cl_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_cl_1 = models.FloatField(db_column='marg_cl__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_cl_2 = models.FloatField(db_column='marg_cl__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_3_field = models.FloatField(db_column='marg_al_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_al_1 = models.FloatField(db_column='marg_al__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_2 = models.FloatField(db_column='marg_al__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_3_field = models.FloatField(db_column='marg_hh_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_hh_1 = models.FloatField(db_column='marg_hh__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_2 = models.FloatField(db_column='marg_hh__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_3_field = models.FloatField(db_column='marg_ot_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_ot_1 = models.FloatField(db_column='marg_ot__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_2 = models.FloatField(db_column='marg_ot__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    margwork_0 = models.FloatField(blank=True, null=True)
    margwork_4 = models.FloatField(blank=True, null=True)
    margwork_5 = models.FloatField(blank=True, null=True)
    marg_cl_0_field = models.FloatField(db_column='marg_cl_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_cl_3 = models.FloatField(db_column='marg_cl__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_cl_4 = models.FloatField(db_column='marg_cl__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_0_field = models.FloatField(db_column='marg_al_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_al_3 = models.FloatField(db_column='marg_al__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_4 = models.FloatField(db_column='marg_al__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_0_field = models.FloatField(db_column='marg_hh_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_hh_3 = models.FloatField(db_column='marg_hh__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_4 = models.FloatField(db_column='marg_hh__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_0_field = models.FloatField(db_column='marg_ot_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_ot_3 = models.FloatField(db_column='marg_ot__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    non_work_p = models.FloatField(blank=True, null=True)
    non_work_m = models.FloatField(blank=True, null=True)
    non_work_f = models.FloatField(blank=True, null=True)
    taluka_nam = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_palghar0'


class IitbWaterLineR1(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiLineStringField(blank=True, null=True)
    id = models.CharField(db_column='ID', max_length=254, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=254, blank=True, null=True)  # Field name made lowercase.
    diameter = models.CharField(db_column='DIAMETER', max_length=254, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='MATERIAL', max_length=254, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iitb_water_line_r1'


class MahaDemography(models.Model):
    fid_1 = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    census_201 = models.BigIntegerField(blank=True, null=True)
    district_c = models.CharField(max_length=254, blank=True, null=True)
    district_n = models.CharField(max_length=254, blank=True, null=True)
    taluka_cod = models.CharField(max_length=254, blank=True, null=True)
    ward = models.CharField(max_length=254, blank=True, null=True)
    area_name = models.CharField(max_length=254, blank=True, null=True)
    tru = models.CharField(max_length=254, blank=True, null=True)
    no_hh = models.FloatField(blank=True, null=True)
    tot_p = models.FloatField(blank=True, null=True)
    tot_m = models.FloatField(blank=True, null=True)
    tot_f = models.FloatField(blank=True, null=True)
    p_06 = models.FloatField(blank=True, null=True)
    m_06 = models.FloatField(blank=True, null=True)
    f_06 = models.FloatField(blank=True, null=True)
    p_sc = models.FloatField(blank=True, null=True)
    m_sc = models.FloatField(blank=True, null=True)
    f_sc = models.FloatField(blank=True, null=True)
    p_st = models.FloatField(blank=True, null=True)
    m_st = models.FloatField(blank=True, null=True)
    f_st = models.FloatField(blank=True, null=True)
    p_lit = models.FloatField(blank=True, null=True)
    m_lit = models.FloatField(blank=True, null=True)
    f_lit = models.FloatField(blank=True, null=True)
    p_ill = models.FloatField(blank=True, null=True)
    m_ill = models.FloatField(blank=True, null=True)
    f_ill = models.FloatField(blank=True, null=True)
    tot_work_p = models.FloatField(blank=True, null=True)
    tot_work_m = models.FloatField(blank=True, null=True)
    tot_work_f = models.FloatField(blank=True, null=True)
    mainwork_p = models.FloatField(blank=True, null=True)
    mainwork_m = models.FloatField(blank=True, null=True)
    mainwork_f = models.FloatField(blank=True, null=True)
    main_cl_p = models.FloatField(blank=True, null=True)
    main_cl_m = models.FloatField(blank=True, null=True)
    main_cl_f = models.FloatField(blank=True, null=True)
    main_al_p = models.FloatField(blank=True, null=True)
    main_al_m = models.FloatField(blank=True, null=True)
    main_al_f = models.FloatField(blank=True, null=True)
    main_hh_p = models.FloatField(blank=True, null=True)
    main_hh_m = models.FloatField(blank=True, null=True)
    main_hh_f = models.FloatField(blank=True, null=True)
    main_ot_p = models.FloatField(blank=True, null=True)
    main_ot_m = models.FloatField(blank=True, null=True)
    main_ot_f = models.FloatField(blank=True, null=True)
    margwork_p = models.FloatField(blank=True, null=True)
    margwork_m = models.FloatField(blank=True, null=True)
    margwork_f = models.FloatField(blank=True, null=True)
    marg_cl_p = models.FloatField(blank=True, null=True)
    marg_cl_m = models.FloatField(blank=True, null=True)
    marg_cl_f = models.FloatField(blank=True, null=True)
    marg_al_p = models.FloatField(blank=True, null=True)
    marg_al_m = models.FloatField(blank=True, null=True)
    marg_al_f = models.FloatField(blank=True, null=True)
    marg_hh_p = models.FloatField(blank=True, null=True)
    marg_hh_m = models.FloatField(blank=True, null=True)
    marg_hh_f = models.FloatField(blank=True, null=True)
    marg_ot_p = models.FloatField(blank=True, null=True)
    marg_ot_m = models.FloatField(blank=True, null=True)
    marg_ot_f = models.FloatField(blank=True, null=True)
    margwork_3 = models.FloatField(blank=True, null=True)
    margwork_1 = models.FloatField(blank=True, null=True)
    margwork_2 = models.FloatField(blank=True, null=True)
    marg_cl_3_field = models.FloatField(db_column='marg_cl_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_cl_1 = models.FloatField(db_column='marg_cl__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_cl_2 = models.FloatField(db_column='marg_cl__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_3_field = models.FloatField(db_column='marg_al_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_al_1 = models.FloatField(db_column='marg_al__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_2 = models.FloatField(db_column='marg_al__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_3_field = models.FloatField(db_column='marg_hh_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_hh_1 = models.FloatField(db_column='marg_hh__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_2 = models.FloatField(db_column='marg_hh__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_3_field = models.FloatField(db_column='marg_ot_3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_ot_1 = models.FloatField(db_column='marg_ot__1', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_2 = models.FloatField(db_column='marg_ot__2', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    margwork_0 = models.FloatField(blank=True, null=True)
    margwork_4 = models.FloatField(blank=True, null=True)
    margwork_5 = models.FloatField(blank=True, null=True)
    marg_cl_0_field = models.FloatField(db_column='marg_cl_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_cl_3 = models.FloatField(db_column='marg_cl__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_cl_4 = models.FloatField(db_column='marg_cl__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_0_field = models.FloatField(db_column='marg_al_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_al_3 = models.FloatField(db_column='marg_al__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_4 = models.FloatField(db_column='marg_al__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_0_field = models.FloatField(db_column='marg_hh_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_hh_3 = models.FloatField(db_column='marg_hh__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_4 = models.FloatField(db_column='marg_hh__4', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_0_field = models.FloatField(db_column='marg_ot_0_', blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_ot_3 = models.FloatField(db_column='marg_ot__3', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    non_work_p = models.FloatField(blank=True, null=True)
    non_work_m = models.FloatField(blank=True, null=True)
    non_work_f = models.FloatField(blank=True, null=True)
    taluka_nam = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maha_demography'


class Mokhada(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    id_0 = models.BigIntegerField(db_column='ID_0', blank=True, null=True)  # Field name made lowercase.
    iso = models.CharField(db_column='ISO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_0 = models.CharField(db_column='NAME_0', max_length=75, blank=True, null=True)  # Field name made lowercase.
    id_1 = models.BigIntegerField(db_column='ID_1', blank=True, null=True)  # Field name made lowercase.
    name_1 = models.CharField(db_column='NAME_1', max_length=75, blank=True, null=True)  # Field name made lowercase.
    id_2 = models.BigIntegerField(db_column='ID_2', blank=True, null=True)  # Field name made lowercase.
    name_2 = models.CharField(db_column='NAME_2', max_length=75, blank=True, null=True)  # Field name made lowercase.
    id_3 = models.BigIntegerField(db_column='ID_3', blank=True, null=True)  # Field name made lowercase.
    name_3 = models.CharField(db_column='NAME_3', max_length=75, blank=True, null=True)  # Field name made lowercase.
    type_3 = models.CharField(db_column='TYPE_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    engtype_3 = models.CharField(db_column='ENGTYPE_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nl_name_3 = models.CharField(db_column='NL_NAME_3', max_length=75, blank=True, null=True)  # Field name made lowercase.
    varname_3 = models.CharField(db_column='VARNAME_3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orig_ogc_f = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mokhada'


class PalgarhBlock(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    id = models.CharField(max_length=254, blank=True, null=True)
    tal_name = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'palgarh_block'


class PalgarhTaluka(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    t_name = models.CharField(max_length=254, blank=True, null=True)
    d_name = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'palgarh_taluka'


class PalgarhTaluka0(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    t_name = models.CharField(max_length=254, blank=True, null=True)
    d_name = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'palgarh_taluka0'


class Stress(models.Model):
    fid_1 = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    maha_gvmp_field = models.IntegerField(db_column='MAHA_GVMP_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    maha_gvmp1 = models.IntegerField(db_column='MAHA_GVMP1', blank=True, null=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='CCODE', max_length=254, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=254, blank=True, null=True)  # Field name made lowercase.
    others = models.CharField(db_column='OTHERS', max_length=254, blank=True, null=True)  # Field name made lowercase.
    vil_cd = models.CharField(db_column='VIL_CD', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dst = models.CharField(db_column='DST', max_length=254, blank=True, null=True)  # Field name made lowercase.
    tq = models.CharField(db_column='TQ', max_length=254, blank=True, null=True)  # Field name made lowercase.
    cen_cd = models.CharField(db_column='CEN_CD', max_length=254, blank=True, null=True)  # Field name made lowercase.
    name_e = models.CharField(db_column='NAME_E', max_length=254, blank=True, null=True)  # Field name made lowercase.
    t_code = models.CharField(db_column='T_CODE', max_length=254, blank=True, null=True)  # Field name made lowercase.
    d_name = models.CharField(db_column='D_NAME', max_length=254, blank=True, null=True)  # Field name made lowercase.
    t_name = models.CharField(db_column='T_NAME', max_length=254, blank=True, null=True)  # Field name made lowercase.
    t_name_old = models.CharField(db_column='T_Name_Old', max_length=254, blank=True, null=True)  # Field name made lowercase.
    d_name_old = models.CharField(db_column='D_Name_Old', max_length=254, blank=True, null=True)  # Field name made lowercase.
    d_code = models.CharField(db_column='D_CODE', max_length=254, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=254, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=254, blank=True, null=True)  # Field name made lowercase.
    shape_leng = models.FloatField(db_column='Shape_Leng', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.
    s_village = models.CharField(db_column='S_Village', max_length=254, blank=True, null=True)  # Field name made lowercase.
    s_stress = models.IntegerField(db_column='S_Stress', blank=True, null=True)  # Field name made lowercase.
    s_availabi = models.IntegerField(db_column='S_Availabi', blank=True, null=True)  # Field name made lowercase.
    s_accessib = models.IntegerField(db_column='S_Accessib', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stress'
