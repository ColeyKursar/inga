# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AnnotationTable(models.Model):
    compound_number = models.IntegerField(db_column='Compound_Number')  # Field name made lowercase.
    elemental_form = models.CharField(db_column='Elemental_Form', max_length=25)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Annotation_Table'


class BciIngaFeb2(models.Model):
    ft_id = models.IntegerField(blank=True, null=True)
    iteration = models.IntegerField(blank=True, null=True)
    census = models.IntegerField(blank=True, null=True)
    sp = models.TextField(blank=True, null=True)
    quadrat = models.IntegerField(blank=True, null=True)
    gx = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    gy = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    life_event = models.TextField(blank=True, null=True)
    dbh = models.IntegerField(blank=True, null=True)
    sc = models.IntegerField(blank=True, null=True)
    norm_agb = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    norm_grth = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    an = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    dbht = models.FloatField(blank=True, null=True)
    dbdhcs = models.FloatField(blank=True, null=True)
    cs = models.FloatField(blank=True, null=True)
    dbhcg = models.FloatField(blank=True, null=True)
    cg = models.FloatField(blank=True, null=True)
    dbhcgp = models.FloatField()
    cgp = models.FloatField(blank=True, null=True)
    dbhhetp = models.FloatField()
    hetp = models.FloatField(blank=True, null=True)
    dbhcgd = models.FloatField()
    cgd = models.FloatField(blank=True, null=True)
    dbhcg_chem = models.FloatField(blank=True, null=True)
    cg_chem = models.FloatField(blank=True, null=True)
    dbhcg_dev = models.FloatField(blank=True, null=True)
    cg_dev = models.FloatField(blank=True, null=True)
    dbhcg_ants = models.FloatField(blank=True, null=True)
    cg_ants = models.FloatField(blank=True, null=True)
    dbhcg_hair = models.FloatField(blank=True, null=True)
    cg_hair = models.FloatField(blank=True, null=True)
    dbhcg_phen = models.FloatField(blank=True, null=True)
    cg_phen = models.FloatField(blank=True, null=True)
    dbhcgnd = models.FloatField()
    cg_nd = models.FloatField(blank=True, null=True)
    dbhcg_element = models.FloatField(blank=True, null=True)
    cg_element = models.FloatField(blank=True, null=True)
    dbhcg_leaf = models.FloatField(blank=True, null=True)
    cg_leaf = models.FloatField(blank=True, null=True)
    dbhcg_wood = models.FloatField(blank=True, null=True)
    cg_wood = models.FloatField(blank=True, null=True)
    dbhcg_height = models.FloatField(blank=True, null=True)
    cg_height = models.FloatField(blank=True, null=True)
    grow = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    grow_sap = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    agb = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    max_sc = models.FloatField(blank=True, null=True)
    mort = models.FloatField(blank=True, null=True)
    rec = models.FloatField(blank=True, null=True)
    update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'BCI_INGA_Feb_2'


class BciIngaJan11(models.Model):
    ft_id = models.IntegerField(blank=True, null=True)
    iteration = models.IntegerField(blank=True, null=True)
    census = models.IntegerField(blank=True, null=True)
    sp = models.TextField(blank=True, null=True)
    quadrat = models.IntegerField(blank=True, null=True)
    gx = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    gy = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    life_event = models.TextField(blank=True, null=True)
    dbh = models.IntegerField(blank=True, null=True)
    sc = models.IntegerField(blank=True, null=True)
    norm_agb = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    norm_grth = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    an = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    dbht = models.IntegerField(blank=True, null=True)
    dbdhcs = models.IntegerField(blank=True, null=True)
    dbhcg = models.IntegerField(blank=True, null=True)
    dbhcgp = models.IntegerField()
    dbhhetp = models.IntegerField()
    dbhcgd = models.IntegerField()
    dbhcgnd = models.IntegerField()
    grow = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    grow_sap = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    agb = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    max_sc = models.IntegerField(blank=True, null=True)
    mort = models.IntegerField(blank=True, null=True)
    rec = models.IntegerField(blank=True, null=True)
    update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'BCI_INGA_JAN_11'


class BciIngaNullFeb2(models.Model):
    ft_id = models.IntegerField(blank=True, null=True)
    iteration = models.IntegerField(blank=True, null=True)
    census = models.IntegerField(blank=True, null=True)
    sp = models.TextField(blank=True, null=True)
    quadrat = models.IntegerField(blank=True, null=True)
    gx = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    gy = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    life_event = models.TextField(blank=True, null=True)
    dbh = models.IntegerField(blank=True, null=True)
    sc = models.IntegerField(blank=True, null=True)
    norm_agb = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    norm_grth = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    an = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    dbht = models.FloatField(blank=True, null=True)
    dbdhcs = models.FloatField(blank=True, null=True)
    cs = models.FloatField(blank=True, null=True)
    dbhcg = models.FloatField(blank=True, null=True)
    cg = models.FloatField(blank=True, null=True)
    dbhcgp = models.FloatField()
    cgp = models.FloatField(blank=True, null=True)
    dbhhetp = models.FloatField()
    hetp = models.FloatField(blank=True, null=True)
    dbhcgd = models.FloatField()
    cgd = models.FloatField(blank=True, null=True)
    dbhcg_chem = models.FloatField(blank=True, null=True)
    cg_chem = models.FloatField(blank=True, null=True)
    dbhcg_dev = models.FloatField(blank=True, null=True)
    cg_dev = models.FloatField(blank=True, null=True)
    dbhcg_ants = models.FloatField(blank=True, null=True)
    cg_ants = models.FloatField(blank=True, null=True)
    dbhcg_hair = models.FloatField(blank=True, null=True)
    cg_hair = models.FloatField(blank=True, null=True)
    dbhcg_phen = models.FloatField(blank=True, null=True)
    cg_phen = models.FloatField(blank=True, null=True)
    dbhcgnd = models.FloatField()
    cg_nd = models.FloatField(blank=True, null=True)
    dbhcg_element = models.FloatField(blank=True, null=True)
    cg_element = models.FloatField(blank=True, null=True)
    dbhcg_leaf = models.FloatField(blank=True, null=True)
    cg_leaf = models.FloatField(blank=True, null=True)
    dbhcg_wood = models.FloatField(blank=True, null=True)
    cg_wood = models.FloatField(blank=True, null=True)
    dbhcg_height = models.FloatField(blank=True, null=True)
    cg_height = models.FloatField(blank=True, null=True)
    grow = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    grow_sap = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    agb = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    max_sc = models.FloatField(blank=True, null=True)
    mort = models.FloatField(blank=True, null=True)
    rec = models.FloatField(blank=True, null=True)
    update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'BCI_INGA_NULL_Feb_2'


class BciIngaNullJan11(models.Model):
    ft_id = models.IntegerField(blank=True, null=True)
    iteration = models.IntegerField(blank=True, null=True)
    census = models.IntegerField(blank=True, null=True)
    sp = models.TextField(blank=True, null=True)
    quadrat = models.IntegerField(blank=True, null=True)
    gx = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    gy = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    life_event = models.TextField(blank=True, null=True)
    dbh = models.IntegerField(blank=True, null=True)
    sc = models.IntegerField(blank=True, null=True)
    norm_agb = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    norm_grth = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    an = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    dbht = models.IntegerField(blank=True, null=True)
    dbdhcs = models.IntegerField(blank=True, null=True)
    dbhcg = models.IntegerField(blank=True, null=True)
    dbhcgp = models.IntegerField()
    dbhhetp = models.IntegerField()
    dbhcgd = models.IntegerField()
    dbhcgnd = models.IntegerField()
    grow = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    grow_sap = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    agb = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    max_sc = models.IntegerField(blank=True, null=True)
    mort = models.IntegerField(blank=True, null=True)
    rec = models.IntegerField(blank=True, null=True)
    update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'BCI_INGA_NULL_JAN_11'


class BciCongenConspecPlotAnal(models.Model):
    ft_id = models.IntegerField(blank=True, null=True)
    iteration = models.IntegerField(blank=True, null=True)
    census = models.IntegerField(blank=True, null=True)
    sp = models.TextField(blank=True, null=True)
    quadrat = models.IntegerField(blank=True, null=True)
    gx = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    gy = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    life_event = models.TextField(blank=True, null=True)
    dbh = models.IntegerField(blank=True, null=True)
    sc = models.IntegerField(blank=True, null=True)
    norm_agb = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    norm_grth = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    an = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    ba_tot = models.IntegerField(blank=True, null=True)
    ba_cs = models.IntegerField(blank=True, null=True)
    ba_cg = models.IntegerField(blank=True, null=True)
    grow = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    grow_sap = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    agb = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    max_sc = models.IntegerField(blank=True, null=True)
    mort = models.IntegerField(blank=True, null=True)
    rec = models.IntegerField(blank=True, null=True)
    update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'BCI_congen_conspec_plot_anal'


class BciCongenConspecPlotAnalBackup(models.Model):
    ft_id = models.IntegerField(blank=True, null=True)
    iteration = models.IntegerField(blank=True, null=True)
    census = models.IntegerField(blank=True, null=True)
    sp = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    quadrat = models.IntegerField(blank=True, null=True)
    gx = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    gy = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    life_event = models.TextField(blank=True, null=True)
    dbh = models.IntegerField(blank=True, null=True)
    sc = models.IntegerField(blank=True, null=True)
    norm_agb = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    norm_grth = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    an = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    ba_tot = models.IntegerField(blank=True, null=True)
    ba_cs = models.IntegerField(blank=True, null=True)
    ba_cg = models.IntegerField(blank=True, null=True)
    grow = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    grow_sap = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    agb = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    max_sc = models.IntegerField(blank=True, null=True)
    mort = models.IntegerField(blank=True, null=True)
    rec = models.IntegerField(blank=True, null=True)
    update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'BCI_congen_conspec_plot_anal_backup'


class CompoundTable(models.Model):
    compound_number = models.IntegerField(db_column='Compound_Number')  # Field name made lowercase.
    pc_id = models.CharField(db_column='PC_ID', unique=True, max_length=25)  # Field name made lowercase.
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Compound_table'


class CompoundTableBci(models.Model):
    compound_number = models.IntegerField(db_column='Compound_Number')  # Field name made lowercase.
    pc_id = models.CharField(db_column='PC_ID', unique=True, max_length=25)  # Field name made lowercase.
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Compound_table_BCI'


class CompoundTicTable(models.Model):
    ct_id = models.AutoField(primary_key=True)
    ct_compound_number = models.IntegerField()
    ct_compound_sample = models.CharField(max_length=25)
    ct_tic = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Compound_tic_table'


class CompoundTicTableBci(models.Model):
    ct_id = models.AutoField(primary_key=True)
    ct_compound_number = models.IntegerField()
    ct_compound_sample = models.CharField(max_length=25)
    ct_tic = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Compound_tic_table_BCI'


class ConvertedPaths(models.Model):
    conv_dn = models.CharField(db_column='conv.dn', unique=True, max_length=100)  # Field renamed to remove unsuitable characters.
    filename = models.CharField(max_length=100)
    filepath = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'Converted_paths'


class Expansion(models.Model):
    collectors = models.CharField(db_column='Collectors', max_length=25, blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    species_code = models.CharField(db_column='Species_code', max_length=11)  # Field name made lowercase.
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lh_field = models.IntegerField(db_column='LH#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    location = models.CharField(db_column='Location', max_length=25, blank=True, null=True)  # Field name made lowercase.
    day1 = models.IntegerField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    hour1 = models.IntegerField(db_column='Hour1', blank=True, null=True)  # Field name made lowercase.
    area1 = models.IntegerField(db_column='Area1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    hour2 = models.IntegerField(db_column='Hour2', blank=True, null=True)  # Field name made lowercase.
    age2 = models.IntegerField(db_column='Age2', blank=True, null=True)  # Field name made lowercase.
    area2 = models.IntegerField(db_column='Area2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    hour3 = models.IntegerField(db_column='Hour3', blank=True, null=True)  # Field name made lowercase.
    age3 = models.IntegerField(db_column='Age3', blank=True, null=True)  # Field name made lowercase.
    area3 = models.IntegerField(db_column='Area3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    hour4 = models.IntegerField(db_column='Hour4', blank=True, null=True)  # Field name made lowercase.
    age4 = models.IntegerField(db_column='Age4', blank=True, null=True)  # Field name made lowercase.
    area4 = models.IntegerField(db_column='Area4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    hour5 = models.IntegerField(db_column='Hour5', blank=True, null=True)  # Field name made lowercase.
    age5 = models.IntegerField(db_column='Age5', blank=True, null=True)  # Field name made lowercase.
    area5 = models.IntegerField(db_column='Area5', blank=True, null=True)  # Field name made lowercase.
    final = models.IntegerField(db_column='Final', blank=True, null=True)  # Field name made lowercase.
    age1percent = models.IntegerField(db_column='Age1percent', blank=True, null=True)  # Field name made lowercase.
    dt2 = models.IntegerField(blank=True, null=True)
    age2percent = models.IntegerField(blank=True, null=True)
    dt3 = models.IntegerField(db_column='DT3', blank=True, null=True)  # Field name made lowercase.
    age3percent = models.IntegerField(db_column='Age3percent', blank=True, null=True)  # Field name made lowercase.
    dt4 = models.IntegerField(db_column='DT4', blank=True, null=True)  # Field name made lowercase.
    age4percent = models.IntegerField(db_column='Age4percent', blank=True, null=True)  # Field name made lowercase.
    dt5 = models.IntegerField(db_column='DT5', blank=True, null=True)  # Field name made lowercase.
    age5percent = models.IntegerField(db_column='Age5percent', blank=True, null=True)  # Field name made lowercase.
    x_dt_d_field = models.IntegerField(db_column='x-DT(d)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    x_exp_percent = models.IntegerField(db_column='x-Exp-percent', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    spp = models.IntegerField(blank=True, null=True)
    notes2 = models.IntegerField(db_column='Notes2', blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Expansion'


class Extraction(models.Model):
    chem_field = models.CharField(db_column='Chem#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(max_length=11)
    species_field = models.CharField(db_column='Species#', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    extraction_number = models.IntegerField(db_column='Extraction_Number', unique=True, blank=True, null=True)  # Field name made lowercase.
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    day = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=5, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    extraction_method = models.FloatField(db_column='Extraction_Method', blank=True, null=True)  # Field name made lowercase.
    chemist = models.CharField(db_column='Chemist', max_length=4, blank=True, null=True)  # Field name made lowercase.
    notebook_number = models.IntegerField(db_column='Notebook_Number', blank=True, null=True)  # Field name made lowercase.
    extraction_notebook_number = models.IntegerField(db_column='Extraction_Notebook_Number', blank=True, null=True)  # Field name made lowercase.
    page_number = models.IntegerField(db_column='Page_Number', blank=True, null=True)  # Field name made lowercase.
    parent_extractionnum = models.CharField(db_column='Parent ExtractionNum', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_chem_used = models.CharField(db_column='Other_Chem#_used', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    box_number = models.CharField(db_column='Box_Number', max_length=5, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    file_names_to_be_linked = models.CharField(db_column='File_Names_to_be_linked', max_length=45, blank=True, null=True)  # Field name made lowercase.
    file_names_to_be_linked_2 = models.CharField(db_column='File_Names_to_be_linked_2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    file_location = models.CharField(db_column='File_Location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Extraction'


class Field(models.Model):
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=4, blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(blank=True, null=True)
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    orig_id = models.IntegerField(db_column='Orig_ID')  # Field name made lowercase.
    species_code = models.CharField(db_column='Species_code', max_length=11, blank=True, null=True)  # Field name made lowercase.
    evm = models.TextField(db_column='EvM')  # Field name made lowercase.
    exp_min = models.CharField(db_column='Exp_Min', max_length=12, blank=True, null=True)  # Field name made lowercase.
    exp_max = models.CharField(db_column='Exp_Max', max_length=12, blank=True, null=True)  # Field name made lowercase.
    field_efn = models.IntegerField(db_column='#EFN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_ants = models.IntegerField(db_column='#ants', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    ants_efn = models.DecimalField(db_column='ants_EFN', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    ant_collection_field = models.CharField(db_column='ant_collection#', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_herb = models.IntegerField(db_column='Total#Herb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    a_herbivore_species_code = models.CharField(db_column='a-herbivore_species_code', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    a_herbivores = models.IntegerField(db_column='a-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    b_herbivore_species_code = models.CharField(db_column='b-herbivore_species_code', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    b_herbivores = models.IntegerField(db_column='b-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    c_herbivore_species_code = models.CharField(db_column='c-herbivore_species_code', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    c_herbivores = models.CharField(db_column='c-#herbivores', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    d_herbivore_collection_field = models.CharField(db_column='d-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    d_herbivores = models.IntegerField(db_column='d-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    d_herbivores_total = models.IntegerField(db_column='d-#herbivores_total', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    d_family_field = models.CharField(db_column='d-family?', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    e_herbivore_collection_field = models.CharField(db_column='e-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    e_herbivores = models.CharField(db_column='e-#herbivores', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    e_herbivores_total = models.IntegerField(db_column='e-#herbivores_total', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    e_family_field = models.CharField(db_column='e-family?', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    f_herbivore_collection_field = models.CharField(db_column='f-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    f_herbivores = models.CharField(db_column='f-#herbivores', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    f_herbivores_total = models.IntegerField(db_column='f-#herbivores_total', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    f_family_field = models.CharField(db_column='f-family?', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    g_herbivore_collection_field = models.CharField(db_column='g-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    g_herbivores = models.CharField(db_column='g-#herbivores', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    g_herbivores_total = models.IntegerField(db_column='g-#herbivores_total', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    g_family_field = models.CharField(db_column='g-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    h_herbivore_collection_field = models.CharField(db_column='h-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    h_herbivores = models.IntegerField(db_column='h-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    h_herbivores_total = models.IntegerField(db_column='h-#herbivores_total', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    h_family_field = models.CharField(db_column='h-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    i_herbivore_collection_field = models.CharField(db_column='i-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    i_herbivores = models.IntegerField(db_column='i-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    i_herbivores_total = models.CharField(db_column='i-#herbivores_total', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    i_family_field = models.CharField(db_column='i-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    j_herbivore_collection_field = models.CharField(db_column='j-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    j_herbivores = models.IntegerField(db_column='j-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    j_herbivores_total_observe = models.IntegerField(db_column='j-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    j_family_field = models.CharField(db_column='j-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    k_herbivore_collection_field = models.CharField(db_column='k-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    k_herbivores = models.IntegerField(db_column='k-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_herbivores_total_observe = models.IntegerField(db_column='k-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_family_field = models.CharField(db_column='k-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    l_herbivore_collection_field = models.CharField(db_column='l-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    l_herbivores = models.IntegerField(db_column='l-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    l_herbivores_total_observe = models.IntegerField(db_column='l-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    l_family_field = models.CharField(db_column='l-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    m_herbivore_collection_field = models.CharField(db_column='m-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    m_herbivores = models.IntegerField(db_column='m-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    m_herbivores_total_observe = models.IntegerField(db_column='m-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    m_family_field = models.CharField(db_column='m-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    n_herbivore_collection_field = models.CharField(db_column='n-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    n_herbivores = models.IntegerField(db_column='n-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_herbivores_total_observe = models.IntegerField(db_column='n-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_family_field = models.CharField(db_column='n-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    o_herbivore_collection_field = models.CharField(db_column='o-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    o_herbivores = models.IntegerField(db_column='o-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    o_herbivores_total_observe = models.IntegerField(db_column='o-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    o_family_field = models.CharField(db_column='o-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    p_herbivore_collection_field = models.CharField(db_column='p-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    p_herbivores = models.IntegerField(db_column='p-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_herbivores_total_observe = models.IntegerField(db_column='p-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_family_field = models.CharField(db_column='p-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    q_herbivore_collection_field = models.CharField(db_column='q-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    q_herbivores = models.IntegerField(db_column='q-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    q_herbivores_total_observe = models.IntegerField(db_column='q-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    q_family_field = models.CharField(db_column='q-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    r_herbivore_collection_field = models.CharField(db_column='r-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    r_herbivores = models.IntegerField(db_column='r-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_herbivores_total_observe = models.IntegerField(db_column='r-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_family_field = models.CharField(db_column='r-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    s_herbivore_collection_field = models.CharField(db_column='s-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    s_herbivores = models.IntegerField(db_column='s-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_herbivores_total_observe = models.IntegerField(db_column='s-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_family_field = models.CharField(db_column='s-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    t_herbivore_collection_field = models.CharField(db_column='t-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    t_herbivores = models.IntegerField(db_column='t-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    t_herbivores_total_observe = models.IntegerField(db_column='t-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    t_family_field = models.CharField(db_column='t-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    u_herbivore_collection_field = models.CharField(db_column='u-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    u_herbivores = models.IntegerField(db_column='u-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    u_herbivores_total_observe = models.IntegerField(db_column='u-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    u_family_field = models.CharField(db_column='u-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    v_herbivore_collection_field = models.CharField(db_column='v-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    v_herbivores = models.IntegerField(db_column='v-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    v_herbivores_total_observe = models.IntegerField(db_column='v-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    v_family_field = models.CharField(db_column='v-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    w_herbivore_collection_field = models.CharField(db_column='w-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    w_herbivores = models.IntegerField(db_column='w-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    w_herbivores_total_observe = models.IntegerField(db_column='w-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    w_family_field = models.CharField(db_column='w-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    x_herbivore_collection_field = models.CharField(db_column='x-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    x_herbivores = models.IntegerField(db_column='x-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    x_herbivores_total_observe = models.IntegerField(db_column='x-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    x_family_field = models.CharField(db_column='x-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    y_herbivore_collection_field = models.CharField(db_column='y-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    y_herbivores = models.IntegerField(db_column='y-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    y_herbivores_total_observe = models.IntegerField(db_column='y-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    y_family_field = models.CharField(db_column='y-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    z_herbivore_collection_field = models.CharField(db_column='z-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    z_herbivores = models.IntegerField(db_column='z-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    z_herbivores_total_observe = models.IntegerField(db_column='z-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    z_family_field = models.CharField(db_column='z-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    aa_herbivore_collection_field = models.CharField(db_column='aa-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    aa_herbivores = models.IntegerField(db_column='aa-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    aa_herbivores_total_observe = models.IntegerField(db_column='aa-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    aa_family_field = models.CharField(db_column='aa-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ab_herbivore_collection_field = models.CharField(db_column='ab-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ab_herbivores = models.IntegerField(db_column='ab-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ab_herbivores_total_observe = models.IntegerField(db_column='ab-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ab_family_field = models.CharField(db_column='ab-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ac_herbivore_collection_field = models.CharField(db_column='ac-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ac_herbivores = models.IntegerField(db_column='ac-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ac_herbivores_total_observe = models.IntegerField(db_column='ac-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ac_family_field = models.CharField(db_column='ac-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ad_herbivore_collection_field = models.CharField(db_column='ad-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ad_herbivores = models.IntegerField(db_column='ad-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ad_herbivores_total_observe = models.IntegerField(db_column='ad-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ad_family_field = models.CharField(db_column='ad-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ae_herbivore_collection_field = models.CharField(db_column='ae-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ae_herbivores = models.IntegerField(db_column='ae-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ae_herbivores_total_observe = models.IntegerField(db_column='ae-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ae_family_field = models.CharField(db_column='ae-family?', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    af_herbivor_collection_field = models.CharField(db_column='AF-Herbivor_Collection#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    af_herbivores_total_observe = models.IntegerField(db_column='af-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    af_family_field = models.CharField(db_column='af-family?', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    af_herbivores = models.IntegerField(db_column='af-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ag_herbivore_collection_field = models.CharField(db_column='ag-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ag_herbivores = models.IntegerField(db_column='ag-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ag_herbivores_total_observe = models.IntegerField(db_column='ag-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ag_family_field = models.CharField(db_column='ag-family?', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ah_herbivore_collection_field = models.CharField(db_column='ah-herbivore_collection#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ah_herbivores = models.IntegerField(db_column='ah-#herbivores', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ah_herbivores_total_observe = models.IntegerField(db_column='ah-#herbivores_total_observe', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ah_family_field = models.CharField(db_column='ah-family?', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    notes1 = models.CharField(db_column='Notes1', max_length=255)  # Field name made lowercase.
    notes2 = models.CharField(db_column='Notes2', max_length=255)  # Field name made lowercase.
    notes3 = models.CharField(db_column='Notes3', max_length=255)  # Field name made lowercase.
    notes4 = models.CharField(db_column='Notes4', max_length=255)  # Field name made lowercase.
    notes5 = models.CharField(db_column='Notes5', max_length=255)  # Field name made lowercase.
    notes6 = models.CharField(db_column='Notes6', max_length=255)  # Field name made lowercase.
    notes7 = models.CharField(db_column='Notes7', max_length=255)  # Field name made lowercase.
    notes8 = models.CharField(db_column='Notes8', max_length=255)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Field'


class Ident1(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    id1_grupo1 = models.CharField(db_column='Id1_Grupo1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    id1_grupo2 = models.CharField(db_column='Id1_Grupo2', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ident_1'


class Ident2(models.Model):
    id2_id = models.AutoField(db_column='Id2_ID', primary_key=True)  # Field name made lowercase.
    id2_grupo1 = models.CharField(db_column='Id2_grupo1', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ident_2'


class Location(models.Model):
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(db_column='Species_code', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gps = models.IntegerField(db_column='GPS')  # Field name made lowercase.
    trail = models.IntegerField(db_column='Trail')  # Field name made lowercase.
    measure = models.IntegerField(db_column='Measure')  # Field name made lowercase.
    offset = models.IntegerField(db_column='Offset')  # Field name made lowercase.
    side = models.IntegerField(db_column='Side')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'


class Motu(models.Model):
    motu = models.CharField(db_column='MOTU', max_length=25)  # Field name made lowercase.
    analysis = models.CharField(db_column='Analysis', max_length=50)  # Field name made lowercase.
    voucher = models.CharField(db_column='Voucher', unique=True, max_length=25, blank=True, null=True)  # Field name made lowercase.
    sequence = models.CharField(db_column='Sequence', max_length=30, blank=True, null=True)  # Field name made lowercase.
    la_motu = models.CharField(db_column='LA_MOTU', max_length=30)  # Field name made lowercase.
    blasting_family = models.TextField(db_column='Blasting_Family')  # Field name made lowercase.
    blasting_subfamily = models.TextField(db_column='Blasting_Subfamily')  # Field name made lowercase.
    blasting_genus = models.TextField(db_column='Blasting_Genus')  # Field name made lowercase.
    percentage = models.IntegerField(db_column='Percentage')  # Field name made lowercase.
    bin = models.CharField(db_column='BIN', max_length=250)  # Field name made lowercase.
    notes_on_host = models.CharField(db_column='Notes_on_host', max_length=300)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=300)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOTU'


class PcId(models.Model):
    pc_id = models.CharField(db_column='PC_ID', max_length=25)  # Field name made lowercase.
    mz_rt = models.CharField(db_column='MZ_RT', max_length=25)  # Field name made lowercase.
    percent_tic = models.DecimalField(db_column='Percent_TIC', max_digits=20, decimal_places=6)  # Field name made lowercase.
    average_tic = models.FloatField(db_column='Average_Tic')  # Field name made lowercase.
    ms_ms_spec = models.TextField(db_column='MS_MS_Spec', blank=True, null=True)  # Field name made lowercase.
    ms_ms_spec_id = models.IntegerField(db_column='MS_MS_Spec_ID', blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PC_ID'
        unique_together = (('pc_id', 'mz_rt'),)


class PcIdBci(models.Model):
    pc_id = models.CharField(db_column='PC_ID', max_length=25)  # Field name made lowercase.
    mz_rt = models.CharField(db_column='MZ_RT', max_length=25)  # Field name made lowercase.
    percent_tic = models.DecimalField(db_column='Percent_TIC', max_digits=20, decimal_places=6)  # Field name made lowercase.
    average_tic = models.FloatField(db_column='Average_Tic')  # Field name made lowercase.
    ms_ms_spec = models.TextField(db_column='MS_MS_Spec', blank=True, null=True)  # Field name made lowercase.
    ms_ms_spec_id = models.IntegerField(db_column='MS_MS_Spec_ID', blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PC_ID_BCI'
        unique_together = (('pc_id', 'mz_rt'),)


class PeakTableV1(models.Model):
    mz_rt = models.CharField(db_column='MZ_RT', max_length=20)  # Field name made lowercase.
    mz = models.IntegerField(db_column='MZ')  # Field name made lowercase.
    rt = models.IntegerField(db_column='RT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Peak_Table_V1'


class PlantTable(models.Model):
    collectors = models.CharField(db_column='Collectors', max_length=100, blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=12, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=4)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day')  # Field name made lowercase.
    plant_field = models.IntegerField(db_column='Plant#')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(db_column='Species_code', max_length=11, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(max_length=6, blank=True, null=True)
    light = models.CharField(max_length=8, blank=True, null=True)
    height = models.CharField(max_length=25, blank=True, null=True)
    dbh = models.CharField(db_column='DBH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lh = models.CharField(db_column='LH', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dna = models.CharField(db_column='DNA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_dna_sent = models.CharField(db_column='Date_DNA_SENT', max_length=11, blank=True, null=True)  # Field name made lowercase.
    notes_plant = models.CharField(db_column='Notes_Plant', max_length=255, blank=True, null=True)  # Field name made lowercase.
    photo_live = models.CharField(max_length=25, blank=True, null=True)
    photo_dry = models.CharField(max_length=25, blank=True, null=True)
    voucher1 = models.CharField(max_length=5, blank=True, null=True)
    voucher2 = models.CharField(max_length=5, blank=True, null=True)
    voucher3 = models.CharField(max_length=10, blank=True, null=True)
    voucher4 = models.CharField(max_length=10, blank=True, null=True)
    herbarium_sample = models.CharField(max_length=25, blank=True, null=True)
    flower_color = models.CharField(max_length=25, blank=True, null=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    new_leaves = models.IntegerField(db_column='New_Leaves', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plant_Table'
        unique_together = (('site', 'plant_field'),)


class PreliminaryPeakTableBci(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    archivo = models.CharField(max_length=20)
    mz_rt = models.CharField(max_length=20)
    rt_round = models.CharField(max_length=20)
    mz_round = models.CharField(max_length=20)
    mz = models.CharField(max_length=20)
    mzmin = models.CharField(max_length=20)
    mzmax = models.CharField(max_length=20)
    rt = models.CharField(max_length=20)
    rtmin = models.CharField(max_length=20)
    rtmax = models.CharField(max_length=20)
    npeaks = models.CharField(max_length=20)
    blank = models.CharField(db_column='Blank', max_length=20)  # Field name made lowercase.
    ing = models.CharField(db_column='Ing', max_length=20)  # Field name made lowercase.
    bn_1 = models.CharField(db_column='BN_1', max_length=20)  # Field name made lowercase.
    bn_2 = models.CharField(db_column='BN_2', max_length=20)  # Field name made lowercase.
    bn_3 = models.CharField(db_column='BN_3', max_length=20)  # Field name made lowercase.
    ing_1 = models.CharField(db_column='Ing_1', max_length=20)  # Field name made lowercase.
    ing_2 = models.CharField(db_column='Ing_2', max_length=20)  # Field name made lowercase.
    ing_3 = models.CharField(db_column='Ing_3', max_length=20)  # Field name made lowercase.
    ing_4 = models.CharField(db_column='Ing_4', max_length=20)  # Field name made lowercase.
    ing_5 = models.CharField(db_column='Ing_5', max_length=20)  # Field name made lowercase.
    isotopes = models.CharField(max_length=20)
    adduct = models.CharField(max_length=20)
    pcgroup = models.CharField(max_length=20)
    tic_average = models.CharField(db_column='TIC_Average', max_length=20)  # Field name made lowercase.
    tic_average2 = models.CharField(db_column='TIC_Average2', max_length=20)  # Field name made lowercase.
    db_match = models.CharField(db_column='DB_Match', max_length=500)  # Field name made lowercase.
    pc_group_identifier = models.CharField(db_column='PC_Group_Identifier', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preliminary_peak_table_bci'


class ProccessedRtiNeg(models.Model):
    rti = models.CharField(db_column='RTI', max_length=50)  # Field name made lowercase.
    file = models.CharField(db_column='FILE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    batch = models.CharField(db_column='Batch', max_length=6, blank=True, null=True)  # Field name made lowercase.
    injection = models.IntegerField(db_column='Injection', blank=True, null=True)  # Field name made lowercase.
    npeaks = models.IntegerField(blank=True, null=True)
    avg_ppm_abs = models.FloatField(blank=True, null=True)
    avg_ppm = models.FloatField(blank=True, null=True)
    avg_rerror_abs = models.FloatField(blank=True, null=True)
    avg_rerror = models.FloatField(blank=True, null=True)
    avg_tic_int = models.IntegerField(db_column='avg_TIC_int', blank=True, null=True)  # Field name made lowercase.
    avg_sn = models.IntegerField(db_column='avg_SN', blank=True, null=True)  # Field name made lowercase.
    avg_pkwidth = models.FloatField(blank=True, null=True)
    cat_co2 = models.DecimalField(db_column='cat_Co2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cat_1 = models.DecimalField(db_column='Cat_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cat_2 = models.DecimalField(db_column='Cat_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cat_3 = models.DecimalField(db_column='Cat_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mor_1 = models.DecimalField(db_column='Mor_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mor_2 = models.DecimalField(db_column='Mor_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mor_3 = models.DecimalField(db_column='Mor_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mor_4 = models.DecimalField(db_column='Mor_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    trypt_1 = models.DecimalField(db_column='Trypt_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proccessed_RTI_NEG'


class RtiQc(models.Model):
    rti = models.CharField(db_column='RTI', max_length=25)  # Field name made lowercase.
    batch = models.CharField(db_column='Batch', max_length=5)  # Field name made lowercase.
    injection = models.IntegerField(db_column='Injection', blank=True, null=True)  # Field name made lowercase.
    standard = models.CharField(db_column='Standard', max_length=35)  # Field name made lowercase.
    ion_type = models.CharField(max_length=5)
    mz = models.FloatField()
    ppm_abs = models.FloatField()
    ppm = models.FloatField()
    mda_abs = models.FloatField()
    mda = models.FloatField()
    rt_in_min = models.FloatField()
    rerror_abs = models.FloatField()
    rerror = models.FloatField()
    tic_into = models.IntegerField(db_column='TIC_into')  # Field name made lowercase.
    tic_intb = models.IntegerField(db_column='TIC_intb')  # Field name made lowercase.
    tic_maxo = models.IntegerField(db_column='TIC_maxo')  # Field name made lowercase.
    sn = models.IntegerField()
    pkwidth = models.DecimalField(max_digits=5, decimal_places=3)
    file = models.CharField(db_column='FILE', max_length=50)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RTI_QC'


class RtiQcV5Backup(models.Model):
    rti = models.CharField(db_column='RTI', max_length=25)  # Field name made lowercase.
    standard = models.CharField(db_column='Standard', max_length=35)  # Field name made lowercase.
    ion_type = models.CharField(max_length=5)
    mz = models.FloatField()
    ppm_abs = models.FloatField()
    ppm = models.FloatField()
    mda_abs = models.FloatField()
    mda = models.FloatField()
    rt_in_min = models.FloatField()
    rerror_abs = models.FloatField()
    rerror = models.FloatField()
    tic_into = models.IntegerField(db_column='TIC_into')  # Field name made lowercase.
    tic_intb = models.IntegerField(db_column='TIC_intb')  # Field name made lowercase.
    tic_maxo = models.IntegerField(db_column='TIC_maxo')  # Field name made lowercase.
    sn = models.IntegerField()
    file = models.CharField(db_column='FILE', max_length=50)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RTI_QC_V5_backup'


class RtiQcV6Backup(models.Model):
    rti = models.CharField(db_column='RTI', max_length=25)  # Field name made lowercase.
    batch = models.CharField(db_column='Batch', max_length=5)  # Field name made lowercase.
    injection = models.IntegerField(db_column='Injection', blank=True, null=True)  # Field name made lowercase.
    standard = models.CharField(db_column='Standard', max_length=35)  # Field name made lowercase.
    ion_type = models.CharField(max_length=5)
    mz = models.FloatField()
    ppm_abs = models.FloatField()
    ppm = models.FloatField()
    mda_abs = models.FloatField()
    mda = models.FloatField()
    rt_in_min = models.FloatField()
    rerror_abs = models.FloatField()
    rerror = models.FloatField()
    tic_into = models.IntegerField(db_column='TIC_into')  # Field name made lowercase.
    tic_intb = models.IntegerField(db_column='TIC_intb')  # Field name made lowercase.
    tic_maxo = models.IntegerField(db_column='TIC_maxo')  # Field name made lowercase.
    sn = models.IntegerField()
    pkwidth = models.DecimalField(max_digits=5, decimal_places=3)
    file = models.CharField(db_column='FILE', max_length=50)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RTI_QC_V6_backup'


class RtiReports(models.Model):
    rti = models.CharField(db_column='RTI', primary_key=True, max_length=50)  # Field name made lowercase.
    report_link = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'RTI_REPORTS'


class SamplePaths(models.Model):
    raw_dn = models.CharField(db_column='raw.dn', unique=True, max_length=100)  # Field renamed to remove unsuitable characters.
    raw_filename = models.CharField(db_column='raw.filename', max_length=100)  # Field renamed to remove unsuitable characters.
    raw_path = models.CharField(db_column='raw.path', max_length=250)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Sample_Paths'


class Species(models.Model):
    site = models.CharField(max_length=12, blank=True, null=True)
    species_code = models.CharField(max_length=11)
    genus = models.CharField(db_column='Genus', max_length=12, blank=True, null=True)  # Field name made lowercase.
    species_name = models.CharField(db_column='Species_name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    authority = models.CharField(max_length=25, blank=True, null=True)
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Species'


class SpeciesHistorical(models.Model):
    site = models.CharField(max_length=12, blank=True, null=True)
    old_species_number = models.CharField(db_column='Old_Species_Number', max_length=7, blank=True, null=True)  # Field name made lowercase.
    species_code = models.CharField(max_length=11)
    genus = models.CharField(db_column='Genus', max_length=12, blank=True, null=True)  # Field name made lowercase.
    species_name = models.CharField(db_column='Species_name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=45, blank=True, null=True)
    note_chem_anal = models.TextField(db_column='Note_Chem_Anal', blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Species_historical'


class TempDbname(models.Model):
    td_id = models.AutoField(db_column='Td_id', primary_key=True)  # Field name made lowercase.
    td_number = models.IntegerField(db_column='Td_Number')  # Field name made lowercase.
    td_group = models.CharField(db_column='Td_Group', max_length=25)  # Field name made lowercase.
    td_name = models.CharField(db_column='Td_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_DBName'


class TotalTempDiv(models.Model):
    tt_pc_id = models.CharField(max_length=25, blank=True, null=True)
    tt_total = models.FloatField(blank=True, null=True)
    tt_average = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Total_temp_div'


class Tyrosine(models.Model):
    extraction_number = models.IntegerField(db_column='Extraction_Number', unique=True, blank=True, null=True)  # Field name made lowercase.
    percent_tyrosine = models.CharField(db_column='Percent_Tyrosine', max_length=6)  # Field name made lowercase.
    link_to_file = models.CharField(db_column='Link_to_File', max_length=155)  # Field name made lowercase.
    calibration_number = models.IntegerField(db_column='Calibration_Number')  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=11, blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='NOTES', max_length=1000)  # Field name made lowercase.
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Tyrosine'


class TyrosineCalibration(models.Model):
    calibration_number = models.IntegerField(db_column='Calibration_Number')  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=11)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    concentration = models.IntegerField(db_column='Concentration')  # Field name made lowercase.
    area = models.IntegerField(db_column='Area')  # Field name made lowercase.
    m_slope = models.IntegerField()
    b_intercept = models.IntegerField()
    r_squared = models.CharField(db_column='R_squared', max_length=5)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=155)  # Field name made lowercase.
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Tyrosine_Calibration'


class UplcResults(models.Model):
    diva_field = models.CharField(db_column='Diva#', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    file_name = models.CharField(db_column='File_Name', max_length=50)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=10, blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    mode = models.TextField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    sample_type = models.CharField(db_column='Sample_Type', max_length=15)  # Field name made lowercase.
    sample_id = models.CharField(db_column='Sample_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    en_field = models.IntegerField(db_column='EN#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    chem_field = models.CharField(db_column='Chem#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    plant_field = models.CharField(db_column='Plant#', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(max_length=11)
    tune_page = models.CharField(db_column='Tune_Page', max_length=55)  # Field name made lowercase.
    project_name = models.CharField(db_column='Project_Name', max_length=55)  # Field name made lowercase.
    ms_method = models.CharField(db_column='MS_Method', max_length=55)  # Field name made lowercase.
    uplc_method = models.CharField(db_column='UPLC_Method', max_length=55)  # Field name made lowercase.
    ms_mode = models.IntegerField(db_column='MS_Mode', blank=True, null=True)  # Field name made lowercase.
    asoc_blank = models.CharField(db_column='Asoc_Blank', max_length=45, blank=True, null=True)  # Field name made lowercase.
    asoc_rti = models.CharField(db_column='Asoc_RTI', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rti_pass = models.TextField(db_column='RTI_PASS', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=155, blank=True, null=True)  # Field name made lowercase.
    all_inga = models.CharField(db_column='All_Inga', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chemocoding = models.CharField(db_column='Chemocoding', max_length=5, blank=True, null=True)  # Field name made lowercase.
    raw_check = models.TextField(db_column='Raw_Check')  # Field name made lowercase.
    mzxml = models.TextField(db_column='mzXML')  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UPLC_Results'


class UplcResultsBackup(models.Model):
    diva_field = models.CharField(db_column='Diva#', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    file_name = models.CharField(db_column='File_Name', max_length=50)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=10, blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    mode = models.TextField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    sample_type = models.CharField(db_column='Sample_Type', max_length=15)  # Field name made lowercase.
    sample_id = models.CharField(db_column='Sample_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    en_field = models.IntegerField(db_column='EN#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    chem_field = models.CharField(db_column='Chem#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    plant_field = models.CharField(db_column='Plant#', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(max_length=11)
    tune_page = models.CharField(db_column='Tune_Page', max_length=55)  # Field name made lowercase.
    project_name = models.CharField(db_column='Project_Name', max_length=55)  # Field name made lowercase.
    ms_method = models.CharField(db_column='MS_Method', max_length=55)  # Field name made lowercase.
    uplc_method = models.CharField(db_column='UPLC_Method', max_length=55)  # Field name made lowercase.
    ms_mode = models.IntegerField(db_column='MS_Mode', blank=True, null=True)  # Field name made lowercase.
    asoc_blank = models.CharField(db_column='Asoc_Blank', max_length=45, blank=True, null=True)  # Field name made lowercase.
    asoc_rti = models.CharField(db_column='Asoc_RTI', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rti_pass = models.TextField(db_column='RTI_PASS', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=155, blank=True, null=True)  # Field name made lowercase.
    all_inga = models.CharField(db_column='All_Inga', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chemocoding = models.CharField(db_column='Chemocoding', max_length=5, blank=True, null=True)  # Field name made lowercase.
    raw_check = models.TextField(db_column='Raw_Check')  # Field name made lowercase.
    mzxml = models.TextField(db_column='mzXML')  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UPLC_Results_backup'


class UplcResultsBackup2(models.Model):
    diva_field = models.CharField(db_column='Diva#', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    file_name = models.CharField(db_column='File_Name', max_length=30)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=10, blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    mode = models.TextField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    sample_type = models.CharField(db_column='Sample_Type', max_length=15)  # Field name made lowercase.
    sample_id = models.CharField(db_column='Sample_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    en_field = models.IntegerField(db_column='EN#')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    chem_field = models.CharField(db_column='Chem#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    plant_field = models.CharField(db_column='Plant#', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(max_length=11)
    tune_page = models.CharField(db_column='Tune_Page', max_length=55)  # Field name made lowercase.
    project_name = models.CharField(db_column='Project_Name', max_length=55)  # Field name made lowercase.
    ms_method = models.CharField(db_column='MS_Method', max_length=55)  # Field name made lowercase.
    uplc_method = models.CharField(db_column='UPLC_Method', max_length=55)  # Field name made lowercase.
    ms_mode = models.IntegerField(db_column='MS_Mode', blank=True, null=True)  # Field name made lowercase.
    asoc_blank = models.CharField(db_column='Asoc_Blank', max_length=45, blank=True, null=True)  # Field name made lowercase.
    asoc_rti = models.CharField(db_column='Asoc_RTI', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rti_pass = models.TextField(db_column='RTI_PASS', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=155, blank=True, null=True)  # Field name made lowercase.
    all_inga = models.CharField(db_column='All_Inga', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chemocoding = models.CharField(db_column='Chemocoding', max_length=5, blank=True, null=True)  # Field name made lowercase.
    raw_check = models.TextField(db_column='Raw_Check')  # Field name made lowercase.
    mzxml = models.TextField(db_column='mzXML')  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UPLC_Results_backup2'


class UplcPressure(models.Model):
    sample_name = models.CharField(max_length=30)
    max_pressure = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'UPLC_pressure'


class UmbAnalysis(models.Model):
    compound_number = models.CharField(db_column='Compound_Number', max_length=10)  # Field name made lowercase.
    mz_rt = models.CharField(db_column='MZ_RT', max_length=20)  # Field name made lowercase.
    mz_round = models.IntegerField(db_column='MZ_Round')  # Field name made lowercase.
    rt_round = models.IntegerField(db_column='RT_ROUND')  # Field name made lowercase.
    tic_average = models.IntegerField(db_column='TIC_Average')  # Field name made lowercase.
    isotopes = models.CharField(db_column='Isotopes', max_length=100)  # Field name made lowercase.
    adduct = models.CharField(max_length=100)
    pcgroup = models.IntegerField()
    isotope_number = models.IntegerField()
    notes = models.CharField(db_column='Notes', max_length=155)  # Field name made lowercase.
    primary_peak = models.IntegerField(db_column='Primary_Peak')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Umb_Analysis'


class Chemistry(models.Model):
    chem_field = models.CharField(db_column='Chem#', unique=True, max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    site = models.CharField(db_column='Site', max_length=12, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=5, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(db_column='Species_code', max_length=11, blank=True, null=True)  # Field name made lowercase.
    species_field = models.CharField(db_column='Species#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_name = models.CharField(db_column='Species_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(max_length=8, blank=True, null=True)
    light = models.CharField(max_length=8, blank=True, null=True)
    exp_min = models.CharField(db_column='Exp_Min', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exp_max = models.CharField(db_column='Exp_Max', max_length=50, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dbh = models.CharField(db_column='DBH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fwg = models.CharField(db_column='FWg', max_length=25, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=25, blank=True, null=True)  # Field name made lowercase.
    use = models.CharField(db_column='Use', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cur_w = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    vial_w = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    unnused_materialg = models.DecimalField(db_column='Unnused_Materialg', max_digits=6, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    box_field = models.CharField(db_column='Box#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_of_plants = models.CharField(db_column='#_of_plants', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    notes10 = models.CharField(db_column='Notes10', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    extracted = models.TextField(db_column='Extracted')  # Field name made lowercase.
    notes12 = models.CharField(db_column='Notes12', max_length=45, blank=True, null=True)  # Field name made lowercase.
    notes13 = models.CharField(db_column='Notes13', max_length=45, blank=True, null=True)  # Field name made lowercase.
    oldspecies_field = models.CharField(db_column='OldSpecies#', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chemistry'


class Chlorophyll(models.Model):
    site = models.CharField(max_length=12, blank=True, null=True)
    species_code = models.CharField(max_length=11)
    year = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=5, blank=True, null=True)
    day = models.CharField(max_length=3, blank=True, null=True)
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    percent_expansion = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=12, blank=True, null=True)
    light = models.CharField(max_length=5, blank=True, null=True)
    spadd = models.IntegerField(db_column='Spadd')  # Field name made lowercase.
    chl_mg_dm2 = models.DecimalField(db_column='Chl_mg/dm2', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chlorophyll'


class DeleteValue(models.Model):
    dv_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delete_value'


class Efn(models.Model):
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=5, blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=12)  # Field name made lowercase.
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(max_length=11)
    basalmm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    midmm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    apicalmm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    color = models.CharField(db_column='Color', max_length=25, blank=True, null=True)  # Field name made lowercase.
    shape = models.CharField(db_column='Shape', max_length=45, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=12, blank=True, null=True)  # Field name made lowercase.
    xefnmm = models.DecimalField(db_column='xEFNmm', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    notes1 = models.CharField(db_column='Notes1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notes2 = models.CharField(db_column='Notes2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'efn'


class ExtractionWeight(models.Model):
    chem_field = models.CharField(db_column='Chem#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(max_length=11)
    extraction_number = models.IntegerField(db_column='Extraction_Number', blank=True, null=True)  # Field name made lowercase.
    pre_vacuum_dry_weight_g = models.CharField(db_column='Pre-vacuum_dry_weight_g', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    post_vacuum_dry_weight_g = models.DecimalField(db_column='Post-vacuum_dry_weight_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sample_dry_weight_g = models.DecimalField(db_column='Sample_dry_weight_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    processed_fresh_weight_g = models.DecimalField(db_column='Processed_fresh_weight_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    empty_vial_wt = models.DecimalField(db_column='Empty_Vial_Wt', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dry_marc_vial_wt = models.DecimalField(db_column='Dry_Marc+Vial_wt', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    final_marc_weight_g = models.DecimalField(db_column='Final_marc_weight_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    total_extract_mass_g = models.DecimalField(db_column='Total_extract_mass_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    prop_sample_remainging = models.DecimalField(db_column='Prop_Sample_Remainging', max_digits=8, decimal_places=4)  # Field name made lowercase.
    percent_extracted = models.DecimalField(db_column='Percent_Extracted', max_digits=8, decimal_places=4)  # Field name made lowercase.
    date_dried = models.DateField(db_column='Date_Dried', blank=True, null=True)  # Field name made lowercase.
    date_stored = models.DateField(db_column='Date_Stored', blank=True, null=True)  # Field name made lowercase.
    filter_paper_weight_g = models.DecimalField(db_column='Filter_Paper_Weight_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    number_70c_h2o_extract_fraction_g = models.DecimalField(db_column='70C_H2O_extract_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    organic_extractable_split_fraction_g = models.DecimalField(db_column='Organic_Extractable_Split_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    percent_of_volume_that_was_fractionated = models.CharField(db_column='Percent_of_Volume_that_was_fractionated', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lipid_fraction_g = models.DecimalField(db_column='Lipid_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    post_defat_organic_extractable_split_fraction_g = models.DecimalField(db_column='Post_Defat;_Organic_Extractable_Split_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    percent_of_volume_that_was_fractionated_1 = models.CharField(db_column='Percent_of_Volume_that_was_fractionated_1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dowex50h_org_acids_neut_frac_neutralized_w_naoh_g = models.DecimalField(db_column='Dowex50H_Org_acids_neut_frac_Neutralized_w_NaOH_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    dowex50h_organic_acid_plus_neutral_fraction_g = models.DecimalField(db_column='Dowex50H_organic_acid_plus_neutral_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    dowex50h_npaa_fraction_g = models.DecimalField(db_column='Dowex50H_NPAA_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    phenolics_and_saponins_fraction_g = models.DecimalField(db_column='Phenolics_and_Saponins_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    hoh_insoluble_g = models.DecimalField(db_column='HOH_Insoluble_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    ods_100_hoh_fraction_g = models.DecimalField(db_column='ODS:_100%_HOH_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_100_hoh_fraction_blank_hoh_5_g = models.DecimalField(db_column='ODS:_100%_HOH_Fraction_Blank_HOH-5_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_25_meoh_fraction_g = models.DecimalField(db_column='ODS_25%_MeOH_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_35_meoh_fraction_g = models.DecimalField(db_column='ODS_35%_MeOH_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_60_meoh_fraction_g = models.DecimalField(db_column='ODS:_60%_MeOH_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_60_meoh_fraction_blank_60_4_g = models.DecimalField(db_column='ODS:_60%_MeOH_Fraction_Blank_60-4_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_50_meoh_fraction_g = models.DecimalField(db_column='ODS_50%_MeOH_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_100_meoh_fractiong = models.DecimalField(db_column='ODS:_100%_MeOH_Fractiong', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_100_meoh_fraction_blank_100_4_g = models.DecimalField(db_column='ODS:_100%_MeOH_Fraction_Blank_100-4_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_100_acetone_fraction_g = models.DecimalField(db_column='ODS:_100%_Acetone_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marc_70_acetone_fraction_g = models.DecimalField(db_column='Marc:_70%_Acetone_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marc_80_etoh_g = models.DecimalField(db_column='Marc:_80%_EtOH_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marc_70_acetonitrile_g = models.CharField(db_column='Marc:_70%_Acetonitrile_g', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_2_5_acetonitrile_fraction_g = models.DecimalField(db_column='ODS:_2.5%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_5_acetonitrile_fraction_g = models.DecimalField(db_column='ODS:_5%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_7_5_acetonitrile_fraction_g = models.DecimalField(db_column='ODS:_7.5%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_10_acetonitrile_fraction_g = models.DecimalField(db_column='ODS:_10%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_15_acetonitrile_fraction_g = models.DecimalField(db_column='ODS:_15%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_20_acetonitrile_fraction_g = models.DecimalField(db_column='ODS:_20%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_50_acetonitrile_fraction_g = models.DecimalField(db_column='ODS:_50%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_50_acetonitrile_fraction_blank_50_4_g = models.DecimalField(db_column='ODS:_50%_Acetonitrile_Fraction_Blank_50-4_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_60_acetonitrile_fraction_g = models.DecimalField(db_column='ODS_60%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_100_acetonitrile_fraction_g = models.DecimalField(db_column='ODS:_100%_Acetonitrile_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ods_100_acetonitrile_fraction_blank_100_4_g = models.DecimalField(db_column='ODS:_100%_Acetonitrile_Fraction_Blank_100-4_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flavonoid_i_fraction_g = models.DecimalField(db_column='Flavonoid_I_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    flavonoid_ii_fraction_g = models.DecimalField(db_column='Flavonoid_II_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    saponins_fraction_g = models.DecimalField(db_column='Saponins_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    protein_i_fraction_g = models.DecimalField(db_column='Protein_I_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    protein_ii_fraction_g = models.DecimalField(db_column='Protein_II_Fraction_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    other_insolubles_g = models.DecimalField(db_column='Other_insolubles_g', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    total_dry_weight_g = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    tyrosine_content_dry_weight = models.DecimalField(db_column='Tyrosine_Content:_%_Dry_Weight', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    percent_recovery = models.DecimalField(db_column='Percent_recovery', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extraction_weight'


class FeatureTableRawData(models.Model):
    sample = models.CharField(max_length=25)
    species_code_sample = models.CharField(db_column='Species_code_sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rt = models.DecimalField(db_column='RT', max_digits=11, decimal_places=4)  # Field name made lowercase.
    mz = models.DecimalField(db_column='MZ', max_digits=11, decimal_places=4)  # Field name made lowercase.
    pc_id = models.CharField(db_column='PC_ID', max_length=25)  # Field name made lowercase.
    tic = models.DecimalField(db_column='TIC', max_digits=11, decimal_places=4)  # Field name made lowercase.
    date_update = models.DateTimeField(db_column='Date_Update', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feature_table_raw_data'


class FeatureTableRawDataAllBci(models.Model):
    sample = models.CharField(max_length=25)
    species_code_sample = models.CharField(db_column='Species_code_sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rt = models.DecimalField(db_column='RT', max_digits=11, decimal_places=4)  # Field name made lowercase.
    mz = models.DecimalField(db_column='MZ', max_digits=11, decimal_places=4)  # Field name made lowercase.
    pc_id = models.CharField(db_column='PC_ID', max_length=25)  # Field name made lowercase.
    tic = models.DecimalField(db_column='TIC', max_digits=11, decimal_places=4)  # Field name made lowercase.
    date_update = models.DateTimeField(db_column='Date_Update', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feature_table_raw_data_all_BCI'


class FeatureTableRawDataJohanna(models.Model):
    sample = models.CharField(max_length=25)
    species_code_sample = models.CharField(db_column='Species_code_sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rt = models.DecimalField(db_column='RT', max_digits=11, decimal_places=4)  # Field name made lowercase.
    mz = models.DecimalField(db_column='MZ', max_digits=11, decimal_places=4)  # Field name made lowercase.
    pc_id = models.CharField(db_column='PC_ID', max_length=25)  # Field name made lowercase.
    tic = models.DecimalField(db_column='TIC', max_digits=11, decimal_places=4)  # Field name made lowercase.
    date_update = models.DateTimeField(db_column='Date_Update', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feature_table_raw_data_johanna'


class FeatureTableRawDataUmbellifera(models.Model):
    sample = models.CharField(max_length=25)
    species_code_sample = models.CharField(db_column='Species_code_sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rt = models.DecimalField(db_column='RT', max_digits=11, decimal_places=4)  # Field name made lowercase.
    mz = models.DecimalField(db_column='MZ', max_digits=11, decimal_places=4)  # Field name made lowercase.
    pc_id = models.CharField(db_column='PC_ID', max_length=25)  # Field name made lowercase.
    tic = models.DecimalField(db_column='TIC', max_digits=11, decimal_places=4)  # Field name made lowercase.
    date_update = models.DateTimeField(db_column='Date_Update', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feature_table_raw_data_umbellifera'


class FinalMul(models.Model):
    fid_orig = models.IntegerField(db_column='FId_orig', blank=True, null=True)  # Field name made lowercase.
    fid_dest = models.IntegerField(db_column='FId_dest', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'final_mul'


class Hairs(models.Model):
    site = models.CharField(max_length=12, blank=True, null=True)
    year = models.CharField(max_length=5, blank=True, null=True)
    month = models.CharField(max_length=5, blank=True, null=True)
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(db_column='Species_code', max_length=11, blank=True, null=True)  # Field name made lowercase.
    density_top_1_field = models.IntegerField(db_column='Density__Top_1_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    density_top_2_field = models.IntegerField(db_column='Density__Top_2_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    density_top_3_field = models.IntegerField(db_column='Density__Top_3_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    density_top_average_01in2 = models.DecimalField(db_column='Density_top_average__#.01in2', max_digits=8, decimal_places=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    field_primary_vein_top_0_1in = models.IntegerField(db_column='#/primary_vein_top_#/0.1in', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    hairtype1 = models.CharField(db_column='HairType1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    field_2o_vein_top_0_1in = models.IntegerField(db_column='#/2o_vein_top_#/0.1in', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    density_bottom_1_field = models.IntegerField(db_column='Density_Bottom_1_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    density_bottom_2_field = models.IntegerField(db_column='Density_Bottom_2_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    density_bottom_3_field = models.IntegerField(db_column='Density_Bottom_3_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    density_bottom_average_01in2 = models.DecimalField(db_column='Density_bottom_average__#.01in2', max_digits=8, decimal_places=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    field_1o_vein_bottom_0_01in = models.IntegerField(db_column='#/1o__vein_bottom_#/0.01in', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    haritype2 = models.CharField(db_column='HariType2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    length_1o_bottom_mm = models.DecimalField(db_column='Length_1o_Bottom_mm', max_digits=8, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    field_2o_vein_bottom_0_1in = models.DecimalField(db_column='#/2o__vein_bottom_#/0.1in', max_digits=8, decimal_places=6, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    small_hairs_on_top_blade = models.IntegerField(blank=True, null=True)
    small_hairs_on_top_vein = models.IntegerField(blank=True, null=True)
    small_hairs_on_bottom_blade = models.IntegerField(blank=True, null=True)
    small_hairs_on_bottom_vein = models.IntegerField(blank=True, null=True)
    notes1 = models.CharField(db_column='Notes1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes_2 = models.CharField(db_column='Notes_2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hairs'


class Herbivory(models.Model):
    site = models.CharField(db_column='Site', max_length=12, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=4, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=55, blank=True, null=True)  # Field name made lowercase.
    species_code = models.CharField(max_length=11)
    leaves_leaflests = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    x_herbivory = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'herbivory'


class InsertValue(models.Model):
    iv_group = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insert_value'


class InsertValueDet(models.Model):
    iv_group1 = models.CharField(max_length=25, blank=True, null=True)
    iv_group2 = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insert_value_det'


class Lma(models.Model):
    site = models.CharField(max_length=12, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=4, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    plant_field = models.IntegerField(db_column='plant#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(max_length=11)
    age = models.CharField(max_length=10, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    light = models.CharField(max_length=20, blank=True, null=True)
    inches = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    area_cm2 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    dw_g = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    dw_area_g_cm2 = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    drying_method = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lma'


class Multiple(models.Model):
    mul_id_orig = models.IntegerField(blank=True, null=True)
    mul_id_destino = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multiple'


class MultipleValue(models.Model):
    id_orig = models.IntegerField()
    id_destino = models.IntegerField()
    min_rt_dest = models.FloatField()
    rt_orig = models.FloatField()
    max_rt_dest = models.FloatField()

    class Meta:
        managed = False
        db_table = 'multiple_value'


class MultipleValueMz(models.Model):
    m_id_orig = models.IntegerField()
    m_id_destino = models.IntegerField()
    m_min_mz_dest = models.FloatField(blank=True, null=True)
    m_mz_orig = models.FloatField(blank=True, null=True)
    m_max_mz_dest = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multiple_value_mz'


class Nitrogen(models.Model):
    site = models.CharField(db_column='Site', max_length=12)  # Field name made lowercase.
    species_code = models.CharField(max_length=11)
    species_field = models.CharField(db_column='species#', max_length=10, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_name = models.CharField(max_length=50, blank=True, null=True)
    plant_field = models.IntegerField(db_column='plant#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    chemistry_field = models.CharField(db_column='chemistry#', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    age = models.CharField(max_length=10, blank=True, null=True)
    weight_before_grounding_g = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    percentage_of_expansion = models.CharField(max_length=10, blank=True, null=True)
    habitat = models.CharField(max_length=10, blank=True, null=True)
    weight_after_grounding_g = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    sample_number_for_n2_analysis = models.CharField(max_length=16, blank=True, null=True)
    subsample_weight_g = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    percent_n = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nitrogen'


class Site(models.Model):
    site = models.CharField(db_column='Site', max_length=12, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=25, blank=True, null=True)  # Field name made lowercase.
    latitude_degrees = models.CharField(db_column='Latitude_Degrees', max_length=5, blank=True, null=True)  # Field name made lowercase.
    latitude_minutes = models.IntegerField(db_column='Latitude_Minutes', blank=True, null=True)  # Field name made lowercase.
    longitude_degrees = models.CharField(db_column='Longitude_Degrees', max_length=5, blank=True, null=True)  # Field name made lowercase.
    longitude_minutes = models.IntegerField(db_column='Longitude_Minutes', blank=True, null=True)  # Field name made lowercase.
    altitude = models.IntegerField(db_column='Altitude', blank=True, null=True)  # Field name made lowercase.
    temp = models.DecimalField(db_column='Temp', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    annual_rainfall = models.IntegerField(db_column='Annual_Rainfall', blank=True, null=True)  # Field name made lowercase.
    rainfall_seasonality = models.CharField(db_column='Rainfall_Seasonality', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rainfall_seasonality_pdfs = models.CharField(db_column='Rainfall_Seasonality_PDFS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    soils = models.CharField(db_column='Soils', max_length=12, blank=True, null=True)  # Field name made lowercase.
    soils_pdfs = models.CharField(db_column='Soils_PDFS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site'


class Toughness(models.Model):
    site = models.CharField(db_column='Site', max_length=12, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    plant_field = models.IntegerField(db_column='Plant#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    species_code = models.CharField(max_length=11)
    toughness1 = models.IntegerField(db_column='Toughness1', blank=True, null=True)  # Field name made lowercase.
    toughness2 = models.IntegerField(db_column='Toughness2', blank=True, null=True)  # Field name made lowercase.
    toughness3 = models.IntegerField(db_column='Toughness3', blank=True, null=True)  # Field name made lowercase.
    toughness4 = models.IntegerField(db_column='Toughness4', blank=True, null=True)  # Field name made lowercase.
    toughness5 = models.IntegerField(db_column='Toughness5', blank=True, null=True)  # Field name made lowercase.
    toughness6 = models.IntegerField(db_column='Toughness6', blank=True, null=True)  # Field name made lowercase.
    toughness7 = models.IntegerField(db_column='Toughness7', blank=True, null=True)  # Field name made lowercase.
    toughness = models.DecimalField(db_column='Toughness', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    max_toughness = models.IntegerField(db_column='Max_Toughness', blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'toughness'


class UniqueValue(models.Model):
    uv_identidad = models.IntegerField()
    uv_grupo = models.CharField(max_length=20, blank=True, null=True)
    uv_min_rt = models.FloatField(blank=True, null=True)
    uv_rt = models.FloatField(blank=True, null=True)
    uv_max_rt = models.FloatField(blank=True, null=True)
    uv_min_mz = models.FloatField(blank=True, null=True)
    uv_mz = models.FloatField(blank=True, null=True)
    uv_max_mz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unique_value'
