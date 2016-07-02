from django.db import models

class Chemistry(models.Model):
    chemistry_number = models.CharField(max_length=100)
    plant = models.ForeignKey("Plant")
    date = models.DateField()
    size = models.TextField()
    light = models.TextField()
    exp_min = models.TextField()
    exp_max = models.TextField()
    height = models.FloatField()
    dbh = models.TextField()
    fwg = models.TextField()
    age = models.TextField()
    use_field = models.TextField()
    cur_w = models.FloatField()
    vial_w = models.FloatField()
    unused_material = models.FloatField()
    box_number = models.TextField()
    number_plants = models.TextField()
    notes = models.TextField()
    status = models.TextField()
    extracted = models.TextField()

class Chlorophyll(models.Model):
    plant = models.ForeignKey("Plant")
    date = models.DateField()
    percent_exposed = models.IntegerField()
    size = models.TextField()
    light = models.TextField()
    spadd = models.IntegerField()
    chl_mg_dm2 = models.FloatField()
    notes = models.TextField()

class Converted(models.Model):
    converted_file = models.FileField()

class DNA(models.Model):
    sequence = models.TextField()

class Expansion(models.Model):
    plant = models.ForeignKey("Plant")
    date = models.DateField()
    pass

class Extraction(models.Model):
    extraction_number = models.IntegerField(primary_key=True)
    chemistry = models.ForeignKey("Chemistry")
    date = models.DateField()
    method = models.FloatField()
    chemist = models.CharField(max_length=20)
    notebook_number = models.IntegerField()
    extraction_notebook_number = models.IntegerField()
    page_number = models.IntegerField()
    parent_extraction = models.ForeignKey("Extraction")
    other_chemistry = models.ManyToManyField("Chemistry", related_name="other_chemistry")
    box = models.CharField(max_length=20)
    comments = models.TextField()

class ExtractionWeight(models.Model):
    extraction = models.ForeignKey("Extraction")
    attribute = models.CharField(max_length=20)
    weight = models.FloatField()

class ExtrafloralNectaries(models.Model):
    basal_mm = models.FloatField()
    mid_mm = models.FloatField()
    apical_mm = models.FloatField()
    color = models.CharField(max_length=20)
    shape = models.TextField()
    efn_type = models.TextField()
    xEFN_mm = models.FloatField()
    notes = models.TextField()

class Field(models.Model):
    date = models.DateField()
    plant = models.ForeignKey("Plant")
    original_id = models.IntegerField()
    evm = models.TextField()
    exp_min = models.TextField()
    exp_max = models.TextField()
    efn = models.IntegerField()
    ants = models.IntegerField()
    ants_efn = models.FloatField()
    ant_collection = models.TextField()
    total_herbivores = models.IntegerField()
    herbivore_species_observation = models.ManyToManyField("HerbivoreSpeciesObservation")
    herbivore_collection_observation = models.ManyToManyField("HerbivoreCollectionObservation")
    notes = models.TextField()

class HPLCResult(models.Model):
    extraction = models.ForeignKey("Extraction")
    tyrosine = models.IntegerField()

class Hairs(models.Model):
    plant = models.ForeignKey("Plant")
    date = models.DateField()

class HerbivoreCollectionObservation(models.Model):
    voucher = models.ForeignKey("HerbivoreVoucher")
    herbivores = models.IntegerField()
    herbivores_total = models.IntegerField()
    family = models.CharField(max_length=20)

class HerbivoreDNA(models.Model):
    dna = models.TextField()
    voucher = models.ForeignKey("HerbivoreVoucher")

class HerbivorePhotos(models.Model):
    photo = models.FileField()
    voucher = models.ForeignKey("HerbivoreVoucher")

class HerbivoreSpecies(models.Model):
    motu = models.TextField()
    analysis = models.TextField()
    sequence = models.TextField()
    la_motu = models.TextField()
    blasting_family = models.TextField()
    blasting_subfamily = models.TextField()
    blasting_genus = models.TextField()
    percentage = models.IntegerField()
    bin = models.TextField()
    notes_on_host = models.TextField()
    notes = models.TextField()

class HerbivoreSpeciesObservation(models.Model):
    species = models.ForeignKey("HerbivoreSpecies")
    number_herbivores = models.IntegerField()

class HerbivoreVoucher(models.Model):
    species = models.ForeignKey("HerbivoreSpecies")

class Herbivory(models.Model):
    species = models.ForeignKey("PlantSpecies")
    date = models.DateField()
    location = models.ForeignKey("Location")
    leaves_leaflets = models.IntegerField()
    total = models.IntegerField()
    x_herbivory = models.FloatField()

class LeafMassArea(models.Model):
    age = models.TextField()
    size = models.TextField()
    light = models.TextField()
    inches = models.FloatField()
    area = models.FloatField()
    dw_g = models.FloatField()
    dw_area_g = models.FloatField()
    drying_method = models.TextField()

class Location(models.Model):
    plant = models.ForeignKey("Plant")
    gps = models.IntegerField()
    trail = models.IntegerField()
    measure = models.IntegerField()
    offset = models.IntegerField()
    side = models.IntegerField()

class Method(models.Model):
    method_number = models.IntegerField()
    description = models.TextField()

class MethodResult(models.Model):
    method = models.ForeignKey("Method")
    metric = models.TextField()
    measurement = models.FloatField()

class Nitrogen(models.Model):
    chemistry = models.ForeignKey("Chemistry")
    age = models.TextField()
    weight_before_grounding = models.FloatField()
    precentage_of_expansion = models.TextField()
    weight_after_grounding = models.FloatField()
    sample_number_for_nitrogen_analysis = models.TextField()
    subsample_weight = models.FloatField()
    percent_nitrogen = models.FloatField()
    notes = models.TextField()

class Plant(models.Model):
    plant_number = models.IntegerField()
    collectors = models.TextField()
    site = models.ForeignKey("Site")
    date = models.DateTimeField()
    species = models.ForeignKey("PlantSpecies")
    size = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    light = models.CharField(max_length=20)
    dbh = models.TextField()
    lh = models.TextField()
    dna = models.TextField()
    date_dna_sent = models.DateTimeField()
    vouchers = models.ManyToManyField("Voucher")
    herbarium_sample = models.TextField()
    flower_color = models.TextField()
    description = models.TextField()
    new_leaves = models.IntegerField()
    code = models.IntegerField()

class PlantDNA(models.Model):
    dna = models.TextField()
    plant = models.ForeignKey("Plant")

class PlantPhoto(models.Model):
    photo = models.FileField()
    plant = models.ForeignKey("Plant")

class PlantSpecies(models.Model):
    old_species_number = models.TextField()
    species_code = models.TextField()
    genus = models.TextField()
    species_name = models.TextField()
    comment = models.TextField()
    authority = models.TextField()
    note_chemistry_analysis = models.TextField()

class RAW(models.Model):
    raw_file_path = models.FileField()

class RTIQC(models.Model):
    rti = models.TextField()
    members = models.ManyToManyField("RTIQCMember")
    passing = models.BooleanField()

class RTIQCMember(models.Model):
    rt = models.IntegerField()
    ppm = models.IntegerField()
    sn = models.IntegerField()
    pk_wd = models.IntegerField()

class Site(models.Model):
    site_id = models.IntegerField(primary_key = True)
    country = models.TextField()
    latitude_degrees = models.TextField()
    latitude_minutes = models.IntegerField()
    longitude_degrees = models.TextField()
    longitude_minutes = models.IntegerField()
    altitude = models.IntegerField()
    temp = models.FloatField()
    annual_rainfall = models.IntegerField()
    rainfall_seasonality = models.TextField()
    rainfall_seasonality_pdfs = models.TextField()
    soils = models.TextField()
    solid_pdfs = models.TextField()

class Toughness(models.Model):
    plant = models.ForeignKey("Plant")
    date = models.DateField()

class UPLCResult(models.Model):
    raw = models.ForeignKey("RAW")
    converted = models.ForeignKey("Converted")
    diva = models.TextField()
    date = models.DateField()
    mode = models.TextField()
    sample_type = models.TextField()
    sample_id = models.TextField()
    extraction = models.ForeignKey("Extraction")
    tune_page = models.TextField()
    project_name = models.TextField()
    ms_method = models.TextField()
    uplc_method = models.TextField()
    ms_mode = models.IntegerField()
    rti = models.ForeignKey("RTIQC")
    is_text = models.TextField()
    is_ppm = models.IntegerField()
    is_rt = models.IntegerField()
    rt_shift = models.IntegerField()
    is_tic = models.IntegerField()
    is_sn = models.IntegerField()
    notes = models.TextField()
    all_inga = models.TextField()
    chemocoding = models.TextField()

class Voucher(models.Model):
    pass