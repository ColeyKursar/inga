from django.db import models
import datetime

class IngaBase(models.Model):
    updated = models.DateField(auto_now=True)
    generic = models.BooleanField(default=False)

    @classmethod
    def names(self):
        names = ()

        for field in self._meta.get_fields():
            if isinstance(field, models.ForeignKey):
                model = field.rel.to
                fieldstring = field.name + ":"
                names += tuple((fieldstring + name[0], fieldstring + name[1]) for name in model.names())
            else:
                model = self
                names += ((model.__name__ + "." + field.name, model.__name__ + "." + field.name),)

        return tuple(sorted(names, key=lambda tup: tup[1]))

    class Meta:
        abstract = True

class Chemistry(IngaBase):
    chemistry_number = models.CharField(max_length=100)
    plant = models.ForeignKey("Plant")
    date = models.DateField(blank=True, null=True)
    exp_min = models.TextField(blank=True, null=True)
    exp_max = models.TextField(blank=True, null=True)
    
    
    fwg = models.TextField(blank=True, null=True)
    exp_vs_mat = models.TextField(blank=True, null=True)
    use_field = models.TextField(blank=True, null=True)
    cur_w = models.FloatField(blank=True, null=True)
    vial_w = models.FloatField(blank=True, null=True)
    
    box_number = models.TextField(blank=True, null=True)
    
    notes = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    extracted = models.NullBooleanField(default=False)

class Chlorophyll(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField(blank=True, null=True)
    percent_expansion = models.IntegerField(blank=True, null=True)
    
    
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


class ExtrafloralNectaries(IngaBase):
    date = models.DateField(blank=True, null=True)
    plant = models.ForeignKey("Plant")
    basal_mm = models.FloatField(blank=True, null=True)
    mid_mm = models.FloatField(blank=True, null=True)
    apical_mm = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=25, blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    efn_type = models.TextField(blank=True, null=True)
    xEFN_mm = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class FeatureTableRawData(IngaBase):
    sample = models.ForeignKey("UPLCResult")
    species_code_sample = models.CharField(max_length=30)
    RT = models.FloatField()
    MZ = models.FloatField()
    PC_ID = models.CharField(max_length=30)
    TIC = models.FloatField()
    Date_Update = models.DateField()

class Field(IngaBase):
    date = models.DateField()
    plant = models.ForeignKey("Plant")
    original_id = models.CharField(max_length=20)
    exp_vs_mat = models.TextField()
    exp_min = models.TextField()
    exp_max = models.TextField()
    efn = models.IntegerField()
    ants = models.IntegerField()
    ants_efn = models.FloatField()
    ant_collection_number = models.TextField()
    herbivores_present = models.BooleanField()
    notes = models.TextField()

class Hairs(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField()

class HerbivoreCollectionObservation(IngaBase):
    collection_number = models.ForeignKey("HerbivoreCollection")
    field = models.ForeignKey("Field")
    herbivores_collected = models.IntegerField()
    herbivores_total = models.IntegerField()
    preliminary_family = models.CharField(max_length=20)

class HerbivoreDNA(IngaBase):
    marker_gene = models.TextField()
    fasta = models.FileField()
    genbank = models.URLField()
    voucher = models.ForeignKey("HerbivoreCollection")

class HerbivoreSpecies(IngaBase):
    motu = models.ForeignKey('HerbivoreCollection')
    la_motu = models.TextField()
    consensus_sequence = models.TextField()
    blasting_family = models.TextField()
    blasting_subfamily = models.TextField()
    blasting_genus = models.TextField()
    percentage_match_on_BOLD = models.IntegerField()
    bin = models.TextField()
    notes_on_host = models.TextField()
    notes = models.TextField()
    ibol = models.TextField()

class HerbivoreCollection(IngaBase):
    collection_number = models.ForeignKey('HerbivoreCollectionObservation')
    photo = models.FileField()
    analysis = models.CharField(max_length=100)
    motu = models.TextField()

class Herbivory(IngaBase):
    species = models.ForeignKey("PlantSpecies")
    date = models.DateField()
    location = models.ForeignKey("Location", blank=True, null=True)
    leaves_leaflets = models.IntegerField()
    total = models.IntegerField()
    x_herbivory = models.FloatField()

    def save(self):
        self.x_herbivory = self.total / self.leaves_leaflets
        super(Herbivory, self).save()

class HPLCResult(IngaBase):
    extraction = models.ForeignKey("Extraction")
    sample_type = models.CharField(max_length=100)
    file_path = models.FileField()
    project = models.CharField(max_length=100)
    date = models.DateField()
    method = models.CharField(max_length=100)
    column_used = models.CharField(max_length=100)
    tyrosine = models.IntegerField()

class LeafMassArea(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField(default=datetime.datetime.now)
    inches = models.FloatField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    dw_g = models.FloatField(null=True, blank=True)
    dw_area_g = models.FloatField(null=True, blank=True)
    drying_method = models.TextField(null=True, blank=True)

class Location(IngaBase):
    plant = models.ForeignKey("Plant", related_name="the_plant")
    gps = models.IntegerField()
    trail = models.IntegerField()
    measure = models.IntegerField()
    offset = models.IntegerField()
    side = models.IntegerField()

class Method(IngaBase):
    method_number = models.IntegerField()
    description = models.TextField()

class Nitrogen(IngaBase):
    chemistry = models.ForeignKey("Chemistry")
    exp_vs_mat = models.TextField(null=True, blank=True)
    weight_before_grounding = models.FloatField(null=True, blank=True)
    percentage_of_expansion = models.TextField(null=True, blank=True)
    weight_after_grounding = models.FloatField(null=True, blank=True)
    sample_number_for_nitrogen_analysis = models.TextField(null=True, blank=True)
    subsample_weight = models.FloatField(null=True, blank=True)
    percent_nitrogen = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

class Plant(IngaBase):
    plant_number = models.IntegerField(blank=True, null=True)
    collectors = models.TextField(blank=True, null=True)
    site = models.ForeignKey("Site", blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    species_code = models.ForeignKey("PlantSpecies", blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    light = models.CharField(max_length=20, blank=True, null=True)
    dbh = models.TextField(blank=True, null=True)
    living_herbarium = models.TextField(blank=True, null=True)
    dna = models.TextField(blank=True, null=True)
    date_dna_sent = models.DateTimeField(blank=True, null=True)
    vouchers = models.ManyToManyField("Voucher", blank=True)
    herbarium_sample = models.TextField(blank=True, null=True)
    flower_color = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    new_leaves = models.IntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)

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

class PlantVoucher(IngaBase):
    plant = models.ForeignKey("Plant")
    voucher = models.CharField(max_length=10)

class RAW(IngaBase):
    raw_file_path = models.FileField()

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
    toughness = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

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
    notes = models.TextField()
    all_inga = models.TextField()
    chemocoding = models.TextField()

class Voucher(IngaBase):
    pass

class PC_ID(IngaBase):
    PC_ID = models.ForeignKey("FeatureTableRawData")
    MZ_RT = models.TextField(blank=True, null=True)
    Percent_TIC = models.FloatField(blank=True, null=True)
    ms_ms_spec = models.TextField(blank=True, null=True)
    ms_ms_spec_id = models.IntegerField(blank=True, null=True)

class Tyrosine(IngaBase):
    extraction = models.ForeignKey("Extraction")
    percent_tyrosine = models.IntegerField()
    file = models.TextField()
    calibration = models.IntegerField()
    date = models.DateField(null=True, blank=True)
