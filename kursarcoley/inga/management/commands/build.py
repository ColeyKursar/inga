from django.core.management.base import BaseCommand, CommandError
from ._private import BuildUtil


class Command(BaseCommand):
    help = 'Migrates from old inga tables'

    def handle(self, *args, **options):
        util = BuildUtil()

        # print("Building sites")
        # util.build_sites()
        # print("Building species")
        # util.build_plant_species()
        # print("Building plants")
        # util.build_plants()
        # print("Building chemistries")
        # util.build_chemistries()
        # print("Building extractions")
        # util.build_extractions()
        # print("Building extrafloral nectaries")
        # util.build_extrafloralnectaries()
        # print("Building herbivore species")
        # util.build_herbivore_species()

        # print("Building herbivories")
        # util.build_herbivory()
        # print("Building LMA")
        # util.build_lma()
        print("Building nitrogen")
        util.build_nitrogen()
        print("Building toughness")
        util.build_toughness()

        print("Building herbivore species observations")
        util.build_herbivore_species_observation()
        print("Build chlorophylls")
        util.build_chlorophylls()
