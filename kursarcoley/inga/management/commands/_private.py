from oldinga import models as old
from inga import models as inga
import datetime
import pytz


class BuildUtil:
    def build_plant_voucher(self, plant, voucher):
        if voucher is not None and voucher.strip() != "":
            new = inga.PlantVoucher()
            new.plant = plant
            new.voucher = voucher.strip()
            new.save()

    def build_date(self, day, month, year):
        return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    def build_date_from_single(self, date):
        return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    def wire(self, model, **kwargs):
        inexact_kwargs = {}

        for key, value in kwargs.items():
            inexact_kwargs[key + "__iexact"] = str(value).strip()
            if inexact_kwargs[key + "__iexact"] == "Null" or inexact_kwargs[key + "__iexact"] == "None":
                try:
                    generic = model.objects.get(generic=True)
                except model.DoesNotExist:
                    generic = model()
                    generic.generic = True
                    generic.save()

                return generic
            elif inexact_kwargs[key + "__iexact"] == "":
                new = model()
                new.save()
                return new

        try:
            return model.objects.get(**inexact_kwargs)
        except model.MultipleObjectsReturned:
            return model.objects.filter(**inexact_kwargs)[0]
        except model.DoesNotExist:
            new = model()
            new.save()
            return new

    def clear(self):
        inga.Site.objects.all().delete()
        inga.PlantSpecies.objects.all().delete()
        inga.Plant.objects.all().delete()
        inga.Chemistry.objects.all().delete()
        inga.Extraction.objects.all().delete()

    def build_sites(self):
        sites = old.Site.objects.all()
        for idx, site in enumerate(sites):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.Site()
            new.site_id = site.pk
            new.site = site.site
            new.country = site.country
            new.latitude_degrees = site.latitude_degrees
            new.latitude_minutes = site.latitude_minutes
            new.longitude_degrees = site.longitude_degrees
            new.longitude_minutes = site.longitude_minutes
            new.altitude = site.altitude
            new.temp = site.temp
            new.annual_rainfall = site.annual_rainfall
            new.rainfall_seasonality = site.rainfall_seasonality
            new.rainfall_seasonality_pdfs = site.rainfall_seasonality_pdfs
            new.soils = site.soils
            new.soils_pdfs = site.soils_pdfs
            new.save()

    def build_plant_species(self):
        species = old.Species.objects.all()
        for idx, specie in enumerate(species):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.PlantSpecies()
            new.old_species_number = specie.old_species_number
            new.species_code = specie.species_code
            new.genus = specie.genus
            new.species_name = specie.species_name
            new.comment = specie.comment
            new.authority = specie.authority
            new.note_chemistry_analysis = specie.note_chem_anal
            new.save()

    def build_plants(self):
        plants = old.PlantTable.objects.all()
        for idx, plant in enumerate(plants):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.Plant()
            new.plant_number = plant.plant_field
            new.site = self.wire(inga.Site, site=plant.site)
            new.date = self.build_date(plant.day, plant.month, plant.year)
            new.species = self.wire(inga.PlantSpecies, species_code=plant.species_code)
            new.size = plant.size
            new.height = plant.height
            new.light = plant.height
            new.dbh = plant.dbh
            new.lh = plant.lh
            new.date_dna_sent = self.build_date_from_single(plant.date_dna_sent)
            new.herbarium_sample = plant.herbarium_sample
            new.flower_color = plant.flower_color
            new.description = plant.description
            new.new_leaves = plant.new_leaves
            new.code = plant.code
            new.save()

            self.build_plant_voucher(new, plant.voucher1)
            self.build_plant_voucher(new, plant.voucher2)
            self.build_plant_voucher(new, plant.voucher3)
            self.build_plant_voucher(new, plant.voucher4)

    def build_chemistries(self):
        chemistries = old.Chemistry.objects.all()
        for idx, chemistry in enumerate(chemistries):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.Chemistry()
            new.chemistry_number = chemistry.chem_field
            new.plant = self.wire(inga.Plant, plant_number=chemistry.plant_field)
            new.date = self.build_date(chemistry.day, chemistry.month, chemistry.year)
            new.size = chemistry.size
            new.light = chemistry.light
            new.exp_min = chemistry.exp_min
            new.exp_max = chemistry.exp_max
            new.height = chemistry.height
            new.dbh = chemistry.dbh
            new.fwg = chemistry.fwg
            new.age = chemistry.age
            new.use_field = chemistry.use
            new.cur_w = chemistry.cur_w
            new.vial_w = chemistry.vial_w
            new.unused_material = chemistry.unused_materialg
            new.box_number = chemistry.box_field
            new.number_plants = chemistry.field_of_plants
            new.notes = str(chemistry.notes10) + ", " + str(chemistry.notes12) + ", " + str(chemistry.notes13)
            new.status = chemistry.status
            if new.extracted or not new.extracted or new.extracted is not None:
                new.extracted = False
            else:
                new.extracted = chemistry.extracted
            new.save()

    def build_extractions(self):
        extractions = old.Extraction.objects.all()
        for idx, extraction in enumerate(extractions):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.Extraction()
            new.extraction_number = extraction.extraction_number
            new.chemistry = self.wire(inga.Chemistry, chemistry_number=extraction.chem_field)
            new.date = self.build_date(extraction.day, extraction.month, extraction.year)
            new.method = extraction.extraction_method
            new.chemist = extraction.chemist
            new.notebook_number = extraction.notebook_number
            new.extraction_notebook_number = extraction.extraction_notebook_number
            new.page_number = extraction.page_number
            new.box = extraction.box_number
            new.comments = extraction.comments
            new.save()

    def build_chlorophylls(self):
        chlorophylls = old.Chlorophyll.objects.all()
        for idx, chlorophyll in enumerate(chlorophylls):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.Chlorophyll()
            new.plant = self.wire(inga.Plant, plant_number=chlorophyll.plant_field)
            new.date = self.build_date(chlorophyll.day, chlorophyll.month, chlorophyll.year)
            new.percent_exposed = chlorophyll.field_exp
            new.size = chlorophyll.size
            new.light = chlorophyll.light
            new.spadd = chlorophyll.spadd
            new.chl_mg_dm2 = chlorophyll.chl_mg_dm2
            new.notes = chlorophyll.notes
            new.save()

    def build_extrafloralnectaries(self):
        efns = old.Efn.objects.all()
        for idx, efn in enumerate(efns):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.ExtrafloralNectaries()
            new.plant = self.wire(inga.Plant, plant_number=efn.plant_field)
            new.date = self.build_date(1, efn.month, efn.year)
            new.basal_mm = efn.basalmm
            new.mid_mm = efn.midmm
            new.apical_mm = efn.apicalmm
            new.color = efn.color
            new.shape = efn.shape
            new.efn_type = efn.efn_type
            new.xEFN_mm = efn.xefnmm
            if efn.notes1 is None and efn.notes2 is None:
                new.notes = ""
            elif efn.notes1 is None:
                new.notes = efn.notes2
            elif efn.notes2 is None:
                new.notes = efn.notes1
            else:
                new.notes = efn.notes1 + efn.notes2
            new.save()

    def build_herbivore_species(self):
        species = old.Motu.objects.all()
        for idx, specie in enumerate(species):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.HerbivoreSpecies()
            new.motu = specie.motu
            new.analysis = specie.analysis
            new.sequence = specie.sequence
            new.la_motu = specie.la_motu
            new.blasting_family = specie.blasting_family
            new.blasting_subfamily = specie.blasting_subfamily
            new.blasting_genus = specie.blasting_genus
            new.percentage = specie.percentage
            new.bin = specie.bin
            new.notes_on_hotes = specie.notes_on_host
            new.notes = specie.notes
            new.save()

    def build_herbivore_species_observation(self):
        observations = old.Field.objects.all()
        for idx, observation in enumerate(observations):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.HerbivoreSpeciesObservation()
            species_observations = {
                observation.a_herbivore_species_code : observation.a_herbivores,
                observation.b_herbivore_species_code : observation.b_herbivores,
                observation.c_herbivore_species_code : observation.c_herbivores
            }

            for species, count in species_observations.items():
                new.species = self.wire(inga.HerbivoreSpecies, motu=species)
                new.count = count
                new.save()

    def build_herbivore_collection_observation(self):
        pass

    def build_field(self):
        pass

    def build_location(self):
        pass

    def build_herbivory(self):
        herbivories = old.Herbivory.objects.all()
        for idx, herbivory in enumerate(herbivories):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.Herbivory()
            new.species = self.wire(inga.PlantSpecies, species_code=herbivory.species_code)
            new.date = self.build_date("1", herbivory.month, herbivory.year)
            new.location = None
            new.leaves_leaflets = herbivory.leaves_leaflests
            new.total = herbivory.total

            new.save()

    def build_lma(self):
        lmas = old.Lma.objects.all()
        for idx, lma in enumerate(lmas):
            if idx % 100 == 0:
                print(str(idx) + " built")
            new = inga.LeafMassArea()
            new.plant = self.wire(inga.Plant, plant_number=lma.plant_field)
            new.date = self.build_date(lma.day, lma.month, lma.year)
            new.age = lma.age
            new.size = lma.size
            new.light = lma.light
            new.inches = lma.inches
            new.area = lma.area_cm2
            new.dw_g = lma.dw_g
            new.dw_area_g = lma.dw_area_g_cm2
            new.drying_method = lma.drying_method
            print(new.__dict__)
            new.save()

## All traits data:
## Create dummy plants with site and species given
## make sure that the site and species information is intact
## add note to traits where dummy plant # used