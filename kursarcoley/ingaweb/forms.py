from inga.models import Extraction, Chemistry, Plant, PlantSpecies
from django.apps import apps
from django import forms

INGA = apps.get_app_config('inga')
MODELS = apps.get_models()
MODELS = tuple((model.__name__, model.__name__) for model in MODELS)
BOOTSTRAP_CSS = {'class':   'form-control'}

class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
            kwargs.setdefault('label_suffix', '')
            super(BootstrapForm, self).__init__(*args, **kwargs)

class ExtractionForm(BootstrapForm):
    extraction_number = forms.IntegerField(widget=forms.NumberInput(attrs=BOOTSTRAP_CSS))
    date = forms.DateField(widget=forms.DateInput(attrs=BOOTSTRAP_CSS))
    method = forms.FloatField(widget=forms.NumberInput(attrs=BOOTSTRAP_CSS))
    chemist = forms.CharField(widget=forms.TextInput(attrs=BOOTSTRAP_CSS))
    chemistry = forms.CharField(widget=forms.TextInput(attrs=BOOTSTRAP_CSS))
    plant = forms.CharField(widget=forms.TextInput(attrs=BOOTSTRAP_CSS), required=False)
    species = forms.CharField(widget=forms.TextInput(attrs=BOOTSTRAP_CSS), required=False)
    dry_weight = forms.FloatField(widget=forms.NumberInput(attrs=BOOTSTRAP_CSS), required=False)
    empty_vial_weight = forms.FloatField(widget=forms.NumberInput(attrs=BOOTSTRAP_CSS), required=False)
    final_weight = forms.FloatField(widget=forms.NumberInput(attrs=BOOTSTRAP_CSS), required=False)
    dry_marc_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'true'}), required=False)
    mass_extracted = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'true'}), required=False)
    proportion_remaining = forms.FloatField(widget=forms.NumberInput(attrs=BOOTSTRAP_CSS), required=False)
    percent_extracted = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'true'}), required=False)
    box = forms.CharField(widget=forms.TextInput(attrs=BOOTSTRAP_CSS), required=False)
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), required=False)

    def clean(self):
        cleaned_data = super(ExtractionForm, self).clean()
        chemistry_number = cleaned_data.get("chemistry")
        plant_number = cleaned_data.get("plant")
        species_code = cleaned_data.get("species")

        try: 
            chemistry = Chemistry.objects.get(chemistry_number=chemistry_number)
            plant = chemistry.plant
            species = plant.species_code

            if (plant_number != "" and plant_number != plant.plant_number) and (species_code != "" and species_code != species.species_code):
                self.add_error(None, "There is an mismatch between the given chemistry number, plant number, and species code.")
        except Chemistry.DoesNotExist:
            self.add_error('chemistry', 'Chemistry number does not match any known chemistry.')

class BatchCreateForm(BootstrapForm):
    input_file = forms.FileField(widget=forms.FileInput(attrs=BOOTSTRAP_CSS))
    table = forms.CharField(widget=forms.Select(attrs=BOOTSTRAP_CSS, choices=MODELS))


class BatchDefineForm(BootstrapForm):
    batch = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, model_fields, csv_headers, *args, **kwargs):
        super(BatchDefineForm, self).__init__(*args, **kwargs)
        choices = (("", ""), ) + model_fields

        for header in csv_headers:
            self.fields[header] = forms.CharField(widget=forms.Select(attrs=BOOTSTRAP_CSS, choices=choices), required=False)
