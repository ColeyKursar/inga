from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime

class IngaBase(models.Model):
    updated = models.DateField(auto_now=True)
    generic = models.BooleanField(default=False)

    @classmethod
    def names(self, visited=[]):
        visited = set(visited)
        names = ()
        
        for field in self._meta.get_fields():
            if field.is_relation and not field.concrete:
                continue
            elif isinstance(field, models.ForeignKey) and field.rel.to.__name__ not in visited:
                model = field.rel.to
                visited.add(field.rel.to.__name__)
                fieldstring = field.name + ":"
                names += tuple((fieldstring + name[0], fieldstring + name[1])
                               for name in model.names(visited))
            else:
                model_name = self.__name__
                names += ((model_name + "." + field.name, model_name + "." + field.name),)


        return tuple(sorted(names, key=lambda tup: tup[1]))


            def save(self, **kwargs):
        try:
            day = self.__class__._meta.get_field("day")
            month = self.__class__._meta.get_field("month")
            year = self.__class__._meta.get_field("year")
            date = self.__class__._meta.get_field("date")

            if self.day is not None and self.month is not None and self.year is not None:
                self.date = datetime.date(self.year, self.month, self.day)
            elif self.date is not None:
                self.day = self.date.day
                self.month = self.date.month
                self.year = self.date.year
        except:
            pass

        super(IngaBase, self).save(**kwargs)

    class Meta:
        abstract = True

class Chemistry(IngaBase):
    chemistry_number = models.CharField(max_length=100)
    plant = models.ForeignKey("Plant", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
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
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    percent_expansion = models.IntegerField(blank=True, null=True)
    spadd = models.IntegerField(blank=True, null=True)
    chl_mg_dm2 = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class Converted(IngaBase):
    converted_file = models.FileField()

class DNA(IngaBase):
    sequence = models.TextField()

class Expansion(IngaBase):
    collectors = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField()
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    plant = models.ForeignKey("Plant")  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lh_field = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    day1 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    hour1 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    area1 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    day2 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    hour2 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    age2 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    area2 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    day3 = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    hour3 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    age3 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    area3 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    day4 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    hour4 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    age4 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    area4 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    day5 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    hour5 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    age5 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    area5 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    final = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    age1percent = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    dt2 = models.IntegerField(blank=True, null=True)
    age2percent = models.IntegerField(blank=True, null=True)
    dt3 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    age3percent = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    dt4 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    age4percent = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    dt5 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    age5percent = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    x_dt_d_field = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    x_exp_percent = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    spp = models.IntegerField(blank=True, null=True)
    notes2 = models.TextField(blank=True, null=True)  # Field name made lowercase.

class Extraction(IngaBase):
    extraction_number = models.IntegerField(blank=True, null=True)
    chemistry = models.ForeignKey("Chemistry", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    method = models.IntegerField(blank=True, null=True)
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
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    plant = models.ForeignKey("Plant", blank=True, null=True)
    basal_mm = models.FloatField(blank=True, null=True)
    mid_mm = models.FloatField(blank=True, null=True)
    apical_mm = models.FloatField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    efn_type = models.TextField(blank=True, null=True)
    xEFN_mm = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def save(self):
        if self.basal_mm and self.mid_mm and self.apical_mm:
            self.xEFN_mm = (self.basal_mm + self.mid_mm + self.apical_mm) / 3
        super(ExtrafloralNectaries, self).save()

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
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
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
    old_table_id = models.IntegerField(blank=True, null=True)

    def save(self):
        if self.ants and self.efn:
            self.ants_efn = self.ants / self.efn
        super(Field, self).save()

class Hairs(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField()
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    notes = models.TextField(blank=True, null=True)

class HairMeasurement(IngaBase):
    hairs = models.ForeignKey("Hairs")
    measurement_name = models.TextField()
    value = models.FloatField()

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
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
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
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    method = models.TextField()
    column_used = models.TextField()
    tyrosine = models.IntegerField()

class LeafMassArea(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField(default=datetime.datetime.now)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    inches = models.FloatField(null=True, blank=True)
    area_cm2 = models.FloatField(null=True, blank=True)
    dw_g = models.FloatField(null=True, blank=True)
    dw_area_g_cm2 = models.FloatField(null=True, blank=True)
    drying_method = models.TextField(null=True, blank=True)

    def save(self):
        if self.dw_g and self.area_cm2:
            self.dw_area_g_cm2 = self.dw_g / self.area_cm2
        super(LeafMassArea, self).save()

class Location(IngaBase):
    plant = models.ForeignKey("Plant", related_name="the_plant")
    gps = models.IntegerField()
    trail = models.IntegerField()
    measure = models.IntegerField()
    offset = models.IntegerField()
    side = models.IntegerField()

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
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
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

    class Meta:
        unique_together = ('site', 'plant_number', )

class PlantDNA(IngaBase):
    dna = models.TextField()
    plant = models.ForeignKey("Plant")

class PlantPhoto(IngaBase):
    photo = models.FileField()
    plant = models.ForeignKey("Plant")

class PlantSpecies(IngaBase):
    species_code = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    species_name = models.TextField(blank=True, null=True)
    authority = models.TextField(blank=True, null=True)

class PlantSpeciesHistorical(IngaBase):
    old_species_number = models.TextField(blank=True, null=True)
    species_code = models.ForeignKey("PlantSpecies", related_name="historical")
    genus = models.TextField(blank=True, null=True)
    species_name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    note_chemistry_analysis = models.TextField(blank=True, null=True)

class PlantVoucher(IngaBase):
    plant = models.ForeignKey("Plant")
    voucher = models.CharField(max_length=30)

class RAW(IngaBase):
    raw_file_path = models.FileField()

class Site(IngaBase):
    site = models.CharField(max_length=30)
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
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    toughness = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class UPLCResult(IngaBase):
    raw = models.ForeignKey("RAW", blank=True, null=True)
    converted = models.ForeignKey("Converted", blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
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
    blank = models.TextField(blank=True, null=True)
    rti = models.TextField(blank=True, null=True)

class PC_ID(IngaBase):
    PC_ID = models.ForeignKey("FeatureTableRawData")
    MZ_RT = models.TextField(blank=True, null=True)
    Percent_TIC = models.FloatField(blank=True, null=True)
    ms_ms_spec = models.TextField(blank=True, null=True)
    ms_ms_spec_id = models.IntegerField(blank=True, null=True)

class Tyrosine(IngaBase):
    extraction = models.ForeignKey("Extraction")
    percent_tyrosine = models.TextField()
    file = models.TextField()
    calibration = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    notes = models.TextField(null=True, blank=True)
