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
                names += tuple((fieldstring + name[0], fieldstring + name[1])
                               for name in model.names())
            else:
                model = self
                names += ((model.__name__ + "." + field.name, model.__name__ + "." + field.name),)

        return tuple(sorted(names, key=lambda tup: tup[1]))

    class Meta:
        abstract = True

class Chemistry(IngaBase):
    chemistry_number = models.CharField(max_length=100)
    plant = models.ForeignKey("Plant", blank=True, null=True)
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
    plant = models.ForeignKey("Plant", blank=True, null=True)
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
    extraction_number = models.IntegerField(blank=True, null=True)
    chemistry = models.ForeignKey("Chemistry", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    method = models.FloatField(blank=True, null=True)
    chemist = models.TextField(blank=True, null=True)
    notebook_number = models.IntegerField(blank=True, null=True)
    extraction_notebook_number = models.IntegerField(blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    parent_extraction = models.ForeignKey("Extraction", null=True, blank=True)
    other_chemistry = models.ManyToManyField("Chemistry", related_name="other_chemistry", db_constraint=False, blank=True)
    dry_weight = models.FloatField(default=0, null=True, blank=True)
    empty_vial_weight = models.FloatField(default=0, null=True, blank=True)
    final_weight = models.FloatField(default=0, null=True, blank=True)
    dry_marc_weight = models.FloatField(default=0, null=True, blank=True)
    mass_extracted = models.FloatField(default=0, null=True, blank=True)
    proportion_remaining = models.FloatField(default=0, null=True, blank=True)
    percent_extracted = models.FloatField(default=0, null=True, blank=True)
    box = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def save(self):
        if self.final_weight and self.empty_vial_weight and self.dry_weight:
            self.dry_marc_weight = self.final_weight - self.empty_vial_weight
            self.mass_extracted = self.dry_weight - self.dry_marc_weight
            self.percent_extracted = (self.mass_extracted / self.dry_weight) * 100
        super(Extraction, self).save()

class ExtractionResultWeight(IngaBase):
    extraction = models.ForeignKey("Extraction")
    trait = models.TextField()
    measurement = models.FloatField(default=0, null=True, blank=True)


class ExtrafloralNectaries(IngaBase):
    date = models.DateField(blank=True, null=True)
    plant = models.ForeignKey("Plant")
    basal_mm = models.FloatField(blank=True, null=True)
    mid_mm = models.FloatField(blank=True, null=True)
    apical_mm = models.FloatField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    efn_type = models.TextField(blank=True, null=True)
    xEFN_mm = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class FeatureTableRawData(IngaBase):
    sample = models.ForeignKey("UPLCResult", blank=True, null=True)
    species_code_sample = models.CharField(max_length=30, blank=True, null=True)
    RT = models.FloatField(blank=True, null=True)
    MZ = models.FloatField(blank=True, null=True)
    PC_ID = models.CharField(max_length=30, blank=True, null=True)
    TIC = models.FloatField(blank=True, null=True)
    Date_Update = models.DateField(blank=True, null=True)

class Field(IngaBase):
    date = models.DateField(blank=True, null=True)
    plant = models.ForeignKey("Plant", blank=True, null=True)
    original_id = models.CharField(max_length=20, blank=True, null=True)
    exp_vs_mat = models.TextField(blank=True, null=True)
    exp_min = models.TextField(blank=True, null=True)
    exp_max = models.TextField(blank=True, null=True)
    efn = models.IntegerField(blank=True, null=True)
    ants = models.IntegerField(blank=True, null=True)
    ants_efn = models.FloatField(blank=True, null=True)
    ant_collection_number = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class Hairs(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField()

class HerbivoreCollectionObservation(IngaBase):
    collection_number = models.ForeignKey("HerbivoreCollection", blank=True, null=True)
    field = models.ForeignKey("Field")
    herbivores_collected = models.IntegerField(blank=True, null=True)
    herbivores_total = models.IntegerField(blank=True, null=True)
    preliminary_family = models.TextField(blank=True, null=True)

class HerbivoreDNA(IngaBase):
    marker_gene = models.TextField()
    fasta = models.FileField()
    genbank = models.URLField()
    voucher = models.ForeignKey("HerbivoreCollection")

class HerbivoreSpecies(IngaBase):
    motu = models.ForeignKey('HerbivoreCollection', blank=True, null=True)
    la_motu = models.TextField(blank=True, null=True)
    consensus_sequence = models.TextField(blank=True, null=True)
    blasting_family = models.TextField(blank=True, null=True)
    blasting_subfamily = models.TextField(blank=True, null=True)
    blasting_genus = models.TextField(blank=True, null=True)
    percentage_match_on_BOLD = models.IntegerField(blank=True, null=True)
    bin = models.TextField(blank=True, null=True)
    notes_on_host = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    ibol = models.TextField(blank=True, null=True)

class HerbivoreCollection(IngaBase):
    collection_number = models.TextField(blank=True, null=True)
    photo = models.FileField(blank=True, null=True)
    analysis = models.TextField(blank=True, null=True)
    motu = models.TextField(blank=True, null=True)

class Herbivory(IngaBase):
    species = models.ForeignKey("PlantSpecies")
    date = models.DateField()
    location = models.ForeignKey("Location", blank=True, null=True)
    leaves_leaflets = models.IntegerField()
    total = models.IntegerField()
    x_herbivory = models.FloatField()

    def save(self):
        if self.total is None:
            self.total = 0

        if self.leaves_leaflets is None:
            self.leaves_leaflets = 0

        self.x_herbivory = self.total / self.leaves_leaflets
        super(Herbivory, self).save()

class HPLCResult(IngaBase): 
    extraction = models.ForeignKey("Extraction")
    sample_type = models.TextField()
    file_path = models.FileField()
    project = models.TextField()
    date = models.DateField()
    method = models.TextField()
    column_used = models.TextField()
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
    chemistry = models.ForeignKey("Chemistry", null=True, blank=True)
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
    date = models.DateField(blank=True, null=True)
    species_code = models.ForeignKey("PlantSpecies", blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    height = models.TextField(blank=True, null=True)
    light = models.TextField(blank=True, null=True)
    dbh = models.TextField(blank=True, null=True)
    living_herbarium = models.TextField(blank=True, null=True)
    dna = models.TextField(blank=True, null=True)
    date_dna_sent = models.DateField(blank=True, null=True)
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
    voucher = models.CharField(max_length=30)

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
    raw = models.ForeignKey("RAW", blank=True, null=True)
    converted = models.ForeignKey("Converted", blank=True, null=True)
    diva = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    mode = models.TextField(blank=True, null=True)
    sample_type = models.TextField(blank=True, null=True)
    sample_id = models.TextField(blank=True, null=True)
    extraction = models.ForeignKey("Extraction", blank=True, null=True)
    tune_page = models.TextField(blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)
    ms_method = models.TextField(blank=True, null=True)
    uplc_method = models.TextField(blank=True, null=True)
    ms_mode = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    all_inga = models.TextField(blank=True, null=True)
    chemocoding = models.TextField(blank=True, null=True)

class PC_ID(IngaBase):
    PC_ID = models.ForeignKey("FeatureTableRawData")
    MZ_RT = models.TextField(blank=True, null=True)
    Percent_TIC = models.FloatField(blank=True, null=True)
    ms_ms_spec = models.TextField(blank=True, null=True)
    ms_ms_spec_id = models.IntegerField(blank=True, null=True)

class Tyrosine(IngaBase):
    extraction = models.ForeignKey("Extraction")
    percent_tyrosine = models.FloatField()
    file = models.TextField()
    calibration = models.IntegerField()
    date = models.DateField(null=True, blank=True)
