from django.core.management.base import BaseCommand, CommandError
from os.path import abspath, dirname, join
from _private import BuildUtil
import json

class Command(BaseCommand):
    help = 'Migrates from old inga tables'

    def handle(self, *args, **options):
        util = BuildUtil()
        toplevel_dir = dirname(dirname(dirname(dirname(dirname(abspath(__file__))))))
        mapping_file = join(toplevel_dir, "mapping.json")

        with open(mapping_file) as f:
            mappings = json.loads(f.read())

        for model in mappings:
            print("Building " + model)
            util.build(model, mappings[model])
            print("Done! \n")
