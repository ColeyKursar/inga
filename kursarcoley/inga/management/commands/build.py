from django.core.management.base import BaseCommand, CommandError
from ._private import BuildUtil


class Command(BaseCommand):
    help = 'Migrates from old inga tables'

    def handle(self, *args, **options):
        util = BuildUtil()

        print("Building sites")
        util.build_sites()
        print("Building species")
        util.build_plant_species()
        print("Building plants")
        util.build_plants()
        print("Building chemistries")
        util.build_chemistries()
        print("Building extractions")
        util.build_extractions()