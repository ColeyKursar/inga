from django.db import models
import datetime

class IngaBase(models.Model):
    updated = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True

class Chemistry(IngaBase):
    chemistry_number = models.CharField(max_length=100)
    plant = models.ForeignKey("Plant")
    date = models.DateField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    light = models.TextField(blank=True, null=True)
    exp_min = models.TextField(blank=True, null=True)
    exp_max = models.TextField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    dbh = models.TextField(blank=True, null=True)
    fwg = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    use_field = models.TextField(blank=True, null=True)
    cur_w = models.FloatField(blank=True, null=True)
    vial_w = models.FloatField(blank=True, null=True)
    unused_material = models.FloatField(blank=True, null=True)
    box_number = models.TextField(blank=True, null=True)
    number_plants = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    extracted = models.BooleanField(default=False)

class Chlorophyll(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField(blank=True, null=True)
    percent_exposed = models.IntegerField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    light = models.TextField(blank=True, null=True)
    spadd = models.IntegerField(blank=True, null=True)
    chl_mg_dm2 = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class Converted(IngaBase):
    converted_file = models.FileField()

class DNA(IngaBase):
    sequence = models.TextField()

class Extraction(IngaBase):
    extraction_number = models.IntegerField(primary_key=True)
    chemistry = models.ForeignKey("Chemistry")
    date = models.DateField(blank=True, null=True)
    method = models.FloatField(blank=True, null=True)
    chemist = models.CharField(blank=True, null=True, max_length=20)
    notebook_number = models.IntegerField(blank=True, null=True)
    extraction_notebook_number = models.IntegerField(blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    parent_extraction = models.ForeignKey("Extraction", null=True, blank=True)
    other_chemistry = models.ManyToManyField("Chemistry", related_name="other_chemistry", blank=True)
    dry_weight = models.FloatField(default=0, null=True, blank=True)
    empty_vial_weight = models.FloatField(default=0, null=True, blank=True)
    final_weight = models.FloatField(default=0, null=True, blank=True)
    dry_marc_weight = models.FloatField(default=0, null=True, blank=True)
    mass_extracted = models.FloatField(default=0, null=True, blank=True)
    proportion_remaining = models.FloatField(default=0, null=True, blank=True)
    percent_extracted = models.FloatField(default=0, null=True, blank=True)
    box = models.CharField(max_length=20, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def save(self):
        if self.final_weight and self.empty_vial_weight and self.dry_weight:
            self.dry_marc_weight = self.final_weight - self.empty_vial_weight
            self.mass_extracted = self.dry_weight - self.dry_marc_weight
            self.percent_extracted = (self.mass_extracted / self.dry_weight) * 100
        super(Extraction, self).save()

class ExtractionResultWeight(IngaBase):
    extraction = models.ForeignKey("Extraction")
    trait = models.CharField(max_length=100)
    measurement = models.FloatField(default=0, null=True, blank=True)
    # Build long tabe

class ExtrafloralNectaries(IngaBase):
    date = models.DateField(blank=True, null=True)
    plant = models.ForeignKey("Plant", default=0)
    basal_mm = models.FloatField(blank=True, null=True)
    mid_mm = models.FloatField(blank=True, null=True)
    apical_mm = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    efn_type = models.TextField(blank=True, null=True)
    xEFN_mm = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class Expansion(IngaBase):
    pass
    #Database>AllTables>Traits>Expansion>...INDB

class Field(IngaBase):
    date = models.DateField()
    plant = models.ForeignKey("Plant")
    original_id = models.CharField(max_length=20)
    evm = models.TextField()
    exp_min = models.TextField()
    exp_max = models.TextField()
    efn = models.IntegerField()
    ants = models.IntegerField()
    ants_efn = models.FloatField()
    ant_collection = models.TextField()
    total_herbivores = models.IntegerField()
    #herbivore_species_observation = models.ManyToManyField("HerbivoreSpeciesObservation")
    herbivore_collection_observation = models.ManyToManyField("HerbivoreCollectionObservation")
    notes = models.TextField()

class HPLCResult(IngaBase):
    extraction = models.ForeignKey("Extraction")
    tyrosine = models.IntegerField()

class Hairs(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField()
    # hairs

class HerbivoreCollectionObservation(IngaBase):
    voucher = models.ForeignKey("HerbivoreVoucher")
    species_code = models.CharField(max_length=20, default="")
    herbivores = models.IntegerField()
    herbivores_total = models.IntegerField()
    family = models.CharField(max_length=20)

class HerbivoreDNA(IngaBase):
    dna = models.TextField()
    voucher = models.ForeignKey("HerbivoreVoucher")

class HerbivorePhotos(IngaBase):
    photo = models.FileField()
    voucher = models.ForeignKey("HerbivoreVoucher", default=0)

class HerbivoreSpecies(IngaBase):
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

class HerbivoreSpeciesObservation(IngaBase):
    species = models.CharField(max_length=20, null=True, blank=True)
    number_herbivores = models.IntegerField()

class HerbivoreVoucher(IngaBase):
    voucher = models.CharField(max_length=20, default="")
    species = models.ForeignKey("HerbivoreSpecies")

class Herbivory(IngaBase):
    species = models.ForeignKey("PlantSpecies")
    date = models.DateField()
    location = models.ForeignKey("Location")
    leaves_leaflets = models.IntegerField()
    total = models.IntegerField()
    x_herbivory = models.FloatField()

    def save(self):
        x_herbivory = self.total / self.leaves_leaflets;
        super(Herbivory, self).save()

class LeafMassArea(IngaBase):
    plant = models.ForeignKey("Plant", default=0)
    date = models.DateField(default=datetime.datetime.now)
    age = models.TextField()
    size = models.TextField()
    light = models.TextField()
    inches = models.FloatField()
    area = models.FloatField()
    dw_g = models.FloatField()
    dw_area_g = models.FloatField()
    drying_method = models.TextField()

class Location(IngaBase):
    plant = models.ForeignKey("Plant", related_name="plant_num")
    gps = models.IntegerField()
    trail = models.IntegerField()
    measure = models.IntegerField()
    offset = models.IntegerField()
    side = models.IntegerField()

class Method(IngaBase):
    method_number = models.IntegerField()
    description = models.TextField()

class MethodResult(IngaBase):
    method = models.ForeignKey("Method")
    metric = models.TextField()
    measurement = models.FloatField()

class Nitrogen(IngaBase):
    chemistry = models.ForeignKey("Chemistry")
    age = models.TextField()
    weight_before_grounding = models.FloatField()
    percentage_of_expansion = models.TextField()
    weight_after_grounding = models.FloatField()
    sample_number_for_nitrogen_analysis = models.TextField()
    subsample_weight = models.FloatField()
    percent_nitrogen = models.FloatField()
    notes = models.TextField()

class Plant(IngaBase):
    plant_number = models.IntegerField()
    collectors = models.TextField(blank=True, null=True)
    site = models.ForeignKey("Site", blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    species = models.ForeignKey("PlantSpecies", blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    light = models.CharField(max_length=20, blank=True, null=True)
    dbh = models.TextField(blank=True, null=True)
    lh = models.TextField(blank=True, null=True)
    dna = models.TextField(blank=True, null=True)
    date_dna_sent = models.DateTimeField(blank=True, null=True)
    vouchers = models.ManyToManyField("Voucher", blank=True)
    herbarium_sample = models.TextField(blank=True, null=True)
    flower_color = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    new_leaves = models.IntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    #add in photo booleans
    #check if flower color is white, if not, drop it

class PlantDNA(IngaBase):
    dna = models.TextField()
    plant = models.ForeignKey("Plant")

class PlantPhoto(IngaBase):
    photo = models.FileField()
    plant = models.ForeignKey("Plant")

class PlantSpecies(IngaBase):
    old_species_number = models.TextField(blank=True, null=True)
    species_code = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    species_name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    authority = models.TextField(blank=True, null=True)
    note_chemistry_analysis = models.TextField(blank=True, null=True)
    #get new nots

class PlantVoucher(IngaBase):
    plant = models.ForeignKey("Plant")
    voucher = models.CharField(max_length=10)

class RAW(IngaBase):
    raw_file_path = models.FileField()

#rebuild rtiqc

class Site(IngaBase):
    site = models.CharField(max_length=12, blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    latitude_degrees = models.TextField(blank=True, null=True)
    latitude_minutes = models.IntegerField(blank=True, null=True)
    longitude_degrees = models.TextField(blank=True, null=True)
    longitude_minutes = models.IntegerField(blank=True, null=True)
    altitude = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    annual_rainfall = models.IntegerField(blank=True, null=True)
    rainfall_seasonality = models.TextField(blank=True, null=True)
    rainfall_seasonality_pdfs = models.TextField(blank=True, null=True)
    soils = models.TextField(blank=True, null=True)
    solid_pdfs = models.TextField(blank=True, null=True)

class Toughness(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField()

class UPLCResult(IngaBase):
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
    #rti = models.ForeignKey("RTIQC")
    notes = models.TextField()
    all_inga = models.TextField()
    chemocoding = models.TextField()

class Voucher(IngaBase):
    pass

class FeatureTableRawData(IngaBase):
  sample = models.ForeignKey("UPLCResult")
  species_code_sample = models.CharField(max_length=30)
  RT = models.FloatField()
  MZ = models.FloatField()
  PC_ID = models.CharField(max_length=30)
  TIC = models.FloatField()
  Date_Update = models.DateField()


# add in rti_neg and rti_pos and samplepaths
# add in tyrosine and tyrosine_calibration
# alert about zeros
# alert about charfields exactly at length
