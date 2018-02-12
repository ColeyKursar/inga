from django.core.management.base import BaseCommand, CommandError
from os.path import abspath, dirname, join
from ._private import *
import json


BUILD_ORDER = [
#    "Site",
#    "PlantSpecies",
#    "PlantSpeciesHistorical",
#    "Plant",
#    "Chemistry",
#    "Nitrogen",
#    "Chlorophyll",
#    "Extraction",
#    "ExtrafloralNectaries",
#    "Hairs",
#    "HerbivoreCollection",
#    "Field",
#    "HerbivoreCollectionObservation",
#    "HerbivoreSpecies",
#    "Herbivory",
    "LeafMassArea",
    "Location",
    "Tyrosine",
    "UPLCResult",
    "FeatureTableRawData",
    "Toughness",
    "Expansion"
]

class Command(BaseCommand):
    help = 'Migrates from old inga tables'

    def handle(self, *args, **options):
        toplevel_dir = dirname(dirname(dirname(dirname(dirname(abspath(__file__))))))
        mapping_file = join(toplevel_dir, "mapping.json")

        with open(mapping_file) as f:
            mappings = json.loads(f.read())

        for model in BUILD_ORDER:
            print("Building " + model)
            build(model, mappings[model])
            print("Done! \n")
