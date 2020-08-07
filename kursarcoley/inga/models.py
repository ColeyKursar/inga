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

class ClayCats(IngaBase):
    n_hoja = models.IntegerField(blank=True, null=True)
    plant = models.ForeignKey("Plant", blank=True, null=True)
    expanding_leaves = models.TextField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    day_start = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    hour_start = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(23)])
    minute_start = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(59)])
    start_timestamp = models.IntegerField(blank=True, null=True)
    day_end = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    hour_end = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(23)])
    minute_end = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(59)])
    end_timestamp = models.IntegerField(blank=True, null=True)
    attack = models.TextField(blank=True, null=True)
    fallen = models.TextField(blank=True, null=True)
    lost = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        year = self.year if self.year is not None else "2000"
        month = self.month if self.month is not None else "1"
        day_start = self.day_start if self.day_start is not None else "1"
        hour_start = self.hour_start if self.hour_start is not None else "0"
        minute_start = self.minute_start if self.minute_start is not None else "0"
        day_end = self.day_end if self.day_end is not None else "1"
        hour_end = self.hour_end if self.hour_end is not None else "0"
        minute_end = self.minute_end if self.minute_end is not None else "0"

        self.start_timestamp = datetime.datetime(year, month, day=day_start, hour=hour_start, minute=minute_start)
        self.end_timestamp = datetime.datetime(year, month, day=day_end, hour=hour_end, minute=minute_end)

        super(ClayCats, self).save(*args, **kwargs)


class Converted(IngaBase):
    converted_file = models.FileField()

class Dale_Herbivory(IngaBase):
    field = models.ForeignKey("Field", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    measurement_type = models.TextField(blank=True, null=True)
    year_start = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    month_start = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    year_end = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    month_end = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    herbivore_damage = models.IntegerField(blank=True, null=True)

class DNA(IngaBase):
    sequence = models.TextField()

class Expansion(IngaBase):
    collectors = models.CharField(max_length=25, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    plant = models.ForeignKey("Plant")
    lh_field = models.TextField(blank=True, null=True)
    day1 = models.IntegerField(blank=True, null=True)
    hour1 = models.IntegerField(blank=True, null=True)
    area1 = models.IntegerField(blank=True, null=True)
    day2 = models.IntegerField(blank=True, null=True)
    hour2 = models.IntegerField(blank=True, null=True)
    age2 = models.IntegerField(blank=True, null=True)
    area2 = models.IntegerField(blank=True, null=True)
    day3 = models.IntegerField( blank=True, null=True)
    hour3 = models.IntegerField(blank=True, null=True)
    age3 = models.IntegerField(blank=True, null=True)
    area3 = models.IntegerField(blank=True, null=True)
    day4 = models.IntegerField(blank=True, null=True)
    hour4 = models.IntegerField(blank=True, null=True)
    age4 = models.IntegerField(blank=True, null=True)
    area4 = models.IntegerField(blank=True, null=True)
    day5 = models.IntegerField(blank=True, null=True)
    hour5 = models.IntegerField(blank=True, null=True)
    age5 = models.IntegerField(blank=True, null=True)
    area5 = models.IntegerField(blank=True, null=True)
    final = models.IntegerField(blank=True, null=True)
    age1percent = models.IntegerField(blank=True, null=True)
    dt2 = models.IntegerField(blank=True, null=True)
    age2percent = models.IntegerField(blank=True, null=True)
    dt3 = models.IntegerField(blank=True, null=True)
    age3percent = models.IntegerField(blank=True, null=True)
    dt4 = models.IntegerField(blank=True, null=True)
    age4percent = models.IntegerField(blank=True, null=True)
    dt5 = models.IntegerField(blank=True, null=True)
    age5percent = models.IntegerField(blank=True, null=True)
    x_dt_d_field = models.IntegerField(blank=True, null=True)
    x_exp_percent = models.IntegerField(blank=True, null=True)
    spp = models.IntegerField(blank=True, null=True)
    notes2 = models.TextField(blank=True, null=True)

class Extraction(IngaBase):
    extraction_number = models.TextField(blank=True, null=True)
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


    def save(self, **kwargs):
        try:
            final_weight = float(self.final_weight)
            empty_weight = float(self.empty_vial_weight)
            dry_weight = float(self.dry_weight)

            self.dry_marc_weight = final_weight - empty_weight
            self.mass_extracted = dry_weight - self.dry_marc_weight
            self.percent_extracted = (self.mass_extracted / dry_weight) * 100
        except:
            pass

        super(Extraction, self).save(**kwargs)

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

    def save(self, **kwargs):
        efn_measurements = []
        for measurement in [self.basal_mm, self.mid_mm, self.apical_mm]:
            try:
                efn_measurements.append(float(measurement))
            except:
                pass
        if len(efn_measurements) > 0:
            self.xEFN_mm = sum(efn_measurements) / float(len(efn_measurements))
        super(ExtrafloralNectaries, self).save(**kwargs)

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
    census_month = models.IntegerField(blank=True, null=True)
    exp_vs_mat = models.TextField(blank=True, null=True)
    exp_min = models.TextField(blank=True, null=True)
    exp_max = models.TextField(blank=True, null=True)
    efn = models.IntegerField(blank=True, null=True)
    ants = models.IntegerField(blank=True, null=True)
    ants_efn = models.FloatField(blank=True, null=True)
    ant_collection_number = models.TextField(blank=True, null=True)
    num_leaves_still_exp = models.IntegerField(blank=True, null=True)
    num_exp_leaves_new = models.IntegerField(blank=True, null= True)
    num_buds_still_exp = models.IntegerField(blank=True, null= True)
    num_new_buds = models.IntegerField(blank=True, null= True)
    herbivore_collectors = models.TextField(blank=True, null=True)
    nalambre = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    old_table_id = models.IntegerField(blank=True, null=True)
    percent_flush_min = models.IntegerField(blank=True, null=True)
    percent_flush_max = models.IntegerField(blank=True, null=True)
    observation_type = models.TextField(blank=True, null=True)
    observed_dead = models.TextField(blank=True, null=True)
    lost_not_found = models.TextField(blank=True, null=True)
    

    def save(self, **kwargs):
        try:
            ants = float(self.ants)
            efn = float(self.efn)
            self.ants_efn = ants / efn
        except:
            pass
        super(Field, self).save(**kwargs)

class Hairs(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField(blank=True, null=True)
    old_id = models.IntegerField(default=0)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    notes = models.TextField(blank=True, null=True)

class HairMeasurement(IngaBase):
    hairs = models.ForeignKey("Hairs")
    measurement_name = models.TextField()
    value = models.FloatField()

class Herbivore(IngaBase):
    field = models.ForeignKey("Field", blank=True, null=True)
    old_collection_number = models.TextField(blank=True, null=True)
    collection_number = models.TextField(blank=True, null=True)
    herbivores_collected = models.IntegerField(blank=True, null=True)
    herbivores_total = models.IntegerField(blank=True, null=True)
    leaf_expansion = models.TextField(blank=True, null=True)
    order = models.TextField(blank=True, null=True)
    preliminary_family = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    co1_sequence = models.TextField(blank=True, null=True)
    percentage_match_on_BOLD = models.IntegerField(blank=True, null=True)
    bin = models.TextField(blank=True, null=True)
    blasting_family = models.TextField(blank=True, null=True)
    blasting_subfamily = models.TextField(blank=True, null=True)
    blasting_genus = models.TextField(blank=True, null=True)
    blasting_species = models.TextField(blank=True, null=True)
    all_inga_trimmed_21bp = models.TextField(blank=True, null=True)
    la_motu = models.TextField(blank=True, null=True)
    motu_2018 = models.TextField(blank=True, null=True)
    ef1a_sequence = models.TextField(blank=True, null=True)
    wingless_sequence = models.TextField(blank=True, null=True)
    its2_sequence = models.TextField(blank=True, null=True)
    pgd_sequence = models.TextField(blank=True, null=True)

#class HerbivoreDNA(IngaBase):
#    collection_number = models.ForeignKey("Herbivore", blank=True, null=True)
#    marker_gene = models.TextField(blank=True, null=True)
#    sequence_file = models.TextField(blank=True, null=True)
#    percentage_match_on_BOLD = models.IntegerField(blank=True, null=True)
#    bin = models.TextField(blank=True, null=True)
#    blasting_family = models.TextField(blank=True, null=True)
#    blasting_subfamily = models.TextField(blank=True, null=True)
#    blasting_genus = models.TextField(blank=True, null=True)
#
#class HerbivoreCollectionObservation(IngaBase):
#    collection_number = models.ForeignKey("HerbivoreCollection", blank=True, null=True)
#    field = models.ForeignKey("Field")
#    herbivores_collected = models.IntegerField(blank=True, null=True)
#    herbivores_total = models.IntegerField(blank=True, null=True)
#    preliminary_family = models.TextField(blank=True, null=True)
#
#class HerbivoreSpecies(IngaBase):
#    motu = models.ForeignKey('HerbivoreCollection', blank=True, null=True)
#    la_motu = models.TextField(blank=True, null=True)
#    consensus_sequence = models.TextField(blank=True, null=True)
#    blasting_family = models.TextField(blank=True, null=True)
#    blasting_subfamily = models.TextField(blank=True, null=True)
#    blasting_genus = models.TextField(blank=True, null=True)
#    percentage_match_on_BOLD = models.IntegerField(blank=True, null=True)
#    bin = models.TextField(blank=True, null=True)
#    notes_on_host = models.TextField(blank=True, null=True)
#    notes = models.TextField(blank=True, null=True)
#    ibol = models.TextField(blank=True, null=True)
#
#class HerbivoreCollection(IngaBase):
#    collection_number = models.TextField(blank=True, null=True)
#    photo = models.TextField(blank=True, null=True)
#    analysis = models.TextField(blank=True, null=True)
#    motu = models.TextField(blank=True, null=True)

class Herbivory(IngaBase):
    plant = models.ForeignKey("Plant", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    leaves_leaflets = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    x_herbivory = models.FloatField(blank=True, null=True)

    def save(self, **kwargs):
        try:
            total = float(self.total)
            leaves = float(self.leaves_leaflets)
            self.x_herbivory = total / leaves
        except:
            pass
        super(Herbivory, self).save(**kwargs)

class HPLCResult(IngaBase): 
    extraction = models.ForeignKey("Extraction")
    sample_type = models.TextField()
    file_path = models.FileField()
    project = models.TextField()
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    method = models.TextField()
    column_used = models.TextField()
    tyrosine = models.IntegerField() 

class LeafMassArea(IngaBase):
    plant = models.ForeignKey("Plant")
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    inches = models.FloatField(null=True, blank=True)
    area_cm2 = models.FloatField(null=True, blank=True)
    dw_g = models.FloatField(null=True, blank=True)
    dw_area_g_cm2 = models.FloatField(null=True, blank=True)
    drying_method = models.TextField(null=True, blank=True)

    def save(self, **kwargs):
        try:
            dw_g = float(self.dw_g)
            area_cm2 = float(self.area_cm2)
            self.dw_area_g_cm2 = dw_g / area_cm2
        except:
            pass
        super(LeafMassArea, self).save(**kwargs)

class Location(IngaBase):
    plant = models.ForeignKey("Plant", related_name="the_plant")
    species_code = models.ForeignKey("PlantSpecies", blank=True, null=True)
    gx = models.FloatField(blank=True, null=True)
    gy = models.FloatField(blank=True, null=True)
    good_data = models.TextField(blank=True, null=True)
    column = models.FloatField(blank=True, null=True)
    row = models.FloatField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    gps = models.FloatField(blank=True, null=True)
    trail = models.TextField(blank=True, null=True)
    census_order = models.IntegerField(blank=True, null=True)
    measure = models.IntegerField()
    offset = models.IntegerField()
    side = models.TextField(blank=True, null=True)

class Methods(IngaBase):
    method_number = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    location_on_K_drive = models.TextField(null=True, blank=True)

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
    plant_number = models.TextField(blank=True, null=True)
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
    nleaves_survey = models.IntegerField(blank=True, null=True)
    nleaves_total = models.IntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    name_based_on_tag = models.TextField(blank=True, null=True)
    plot_tag = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    census_status = models.TextField(blank=True, null=True)
    observation_type = models.TextField(blank=True, null=True)

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
    chem = models.TextField(blank=True, null=True)
    chem_notes = models.TextField(blank=True, null=True)
    DNA = models.TextField(blank=True, null=True)
    DNA_notes = models.TextField(blank=True, null=True)
    chemotype = models.TextField(blank=True,null=True)
    
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

class RTIQC(IngaBase):
    RTI = models.TextField(blank=True, null=True)
    batch = models.TextField(blank=True, null=True)
    injection = models.TextField(blank=True,null=True)
    standard = models.TextField(blank=True, null=True)
    ion_type = models.TextField(blank=True, null=True)
    mz = models.FloatField(blank=True, null=True)
    ppm_abs = models.FloatField(blank=True, null=True)
    ppm = models.DecimalField(blank=True, null=True, decimal_places=10, max_digits=20)
    mda_abs = models.FloatField(blank=True, null=True)
    mda = models.DecimalField(blank=True, null=True, decimal_places=10, max_digits=20)
    rt_in_min = models.FloatField(blank=True, null= True)
    rerror_abs = models.FloatField(blank=True, null= True)
    rerror = models.FloatField(blank=True, null= True)
    TIC_into = models.FloatField(blank=True, null= True)
    TIC_intb = models.FloatField(blank=True, null= True)
    TIC_maxo = models.FloatField(blank=True, null= True)
    sn = models.IntegerField(blank=True, null=True)
    pkwidth = models.FloatField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)


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
    date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    toughness = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class UPLCResult(IngaBase):
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
    ms_mode = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    all_inga = models.TextField(blank=True, null=True)
    chemocoding = models.TextField(blank=True, null=True)
    raw = models.ForeignKey("RAW", blank=True, null=True)
    mzxml = models.TextField(blank=True, null=True)
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
    percent_tyrosine = models.FloatField(blank=True, null=True)
    file = models.TextField()
    calibration = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    notes = models.TextField(null=True, blank=True)
    keep_or_drop = models.TextField(null=True, blank=True)

class Weather(IngaBase):
    timestamp = models.DateTimeField(null=True, blank=True)
    record = models.IntegerField(blank=True, null=True)
    batt_volt_min = models.FloatField(blank=True, null=True)
    airtc_avg = models.FloatField(blank=True, null=True)
    airtc_std = models.FloatField(blank=True, null=True)
    RH = models.FloatField(blank=True, null=True)
    airtc_2_avg = models.FloatField(blank=True, null=True)
    airtc_2_std = models.FloatField(blank=True, null=True)
    RH_2 = models.FloatField(blank=True, null=True)
    airtc_3_avg = models.FloatField(blank=True, null=True)
    airtc_3_std = models.FloatField(blank=True, null=True)
    RH_3 = models.FloatField(blank=True, null=True)
    slrw_avg = models.FloatField(blank=True, null=True)
    slrw_std = models.FloatField(blank=True, null=True)
    slrmj_tot = models.FloatField(blank=True, null=True)
    slrw_2_avg = models.FloatField(blank=True, null=True)
    slrw_2_std = models.FloatField(blank=True, null=True)
    slrmj_2_tot = models.FloatField(blank=True, null=True)
    rain_mm_tot = models.FloatField(blank=True, null=True)
    srl_num = models.IntegerField(blank=True, null=True)
    prog_name = models.TextField(blank=True, null=True)
    OSVer = models.TextField(blank=True, null=True)
    stat_name = models.TextField(blank=True, null=True)
    msg_var = models.TextField(blank=True, null=True)
    fan_status = models.TextField(blank=True, null=True)
    tach_tot = models.IntegerField(blank=True, null=True)
