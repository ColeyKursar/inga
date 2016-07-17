from oldinga import models as old
from inga import models as inga
import datetime
import pytz


class BuildUtil:
    def build_voucher(self, plant, voucher):
        new = inga.Voucher()
        new.plant = plant
        new.voucher = voucher
        new.save()

    def build_date(self, day, month, year):
        return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    def build_date_from_single(self, date):
        return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    def wire(self, model, **kwargs):
        inexact_kwargs = {}

        for key, value in kwargs.items():
            inexact_kwargs[key + "__iexact"] = str(value).strip()

        try:
            return model.objects.get(**inexact_kwargs)
        except model.MultipleObjectsReturned:
            return model.objects.filter(**inexact_kwargs)[0]

    def clear(self):
        #inga.Site.objects.all().delete()
        #inga.PlantSpecies.objects.all().delete()
        #inga.Plant.objects.all().delete()
        inga.Chemistry.objects.all().delete()

    def build_sites(self):
        sites = old.Site.objects.all()
        for idx,site in enumerate(sites):
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
        for idx,specie in enumerate(species):
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
        for idx,plant in enumerate(plants):
            if idx % 1 == 0:
                print(str(idx) + " built") 
                print("+" + plant.species_code + "+")
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
            self.build_voucher(new, plant.voucher1)
            self.build_voucher(new, plant.voucher2)
            self.build_voucher(new, plant.voucher3)
            self.build_voucher(new, plant.voucher4)
            new.herbarium_sample = plant.herbarium_sample
            new.flower_color = plant.flower_color
            new.description = plant.description
            new.new_leaves = plant.new_leaves
            new.code = plant.code
            new.save()
        
    def build_chemistries(self):
        chemistries = old.Chemistry.objects.all()
        for idx,chemistry in enumerate(chemistries):
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
            new.extracted = chemistry.extracted
            new.save()
