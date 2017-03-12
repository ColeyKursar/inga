from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields.related import RelatedField as Related
from django.db.models import DateField
import json


REFERENCE_TEMPLATE = {"type": "reference",
                      "reference_model": "",
                      "remote_field_name": "",
                      "local_field_name": ""}

VALUE_TEMPLATE = {"type": "value",
                  "field_name": ""}

DATE_TEMPLATE = {"type": "date",
                 "year_field": "",
                 "month_field": "",
                 "day_field": ""}

class Command(BaseCommand):
    help = 'Generates template for conversion'

    def handle(self, *args, **options):
        mappings = {}

        app_models = apps.get_app_config('inga').get_models()
        for model in app_models:
            try:
                mapping = {"origin": ""}
                fields = {}

                for field in model._meta.get_fields():
                    field_mapping = {}
                    if issubclass(field.__class__, Related):
                        field_mapping = REFERENCE_TEMPLATE
                    elif isinstance(field, DateField):
                        field_mapping = DATE_TEMPLATE
                    else:
                        field_mapping = VALUE_TEMPLATE

                    fields[field.name] = field_mapping



                mapping["fields"] = fields
                mappings[model.__name__] = mapping
            except AlreadyRegistered:
                pass

        print json.dumps(mappings)
