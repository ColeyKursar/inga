from inga.models import Extraction, Chemistry, Plant, PlantSpecies
from django import forms

class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
            kwargs.setdefault('label_suffix', '')
            super(BootstrapForm, self).__init__(*args, **kwargs)

class ExtractionForm(BootstrapForm):
    extraction_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    method = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    chemist = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    chemistry = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    plant = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    species = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    dry_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    empty_vial_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    final_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    dry_marc_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'true'}), required=False)
    mass_extracted = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'true'}), required=False)
    proportion_remaining = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    percent_extracted = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'true'}), required=False)
    box = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), required=False)

    def clean(self):
        cleaned_data = super(ExtractionForm, self).clean()
        chemistry_number = cleaned_data.get("chemistry")
        plant_number = cleaned_data.get("plant")
        species_code = cleaned_data.get("species")

        try: 
            chemistry = Chemistry.objects.get(chemistry_number=chemistry_number)
            plant = chemistry.plant
            species = plant.species

            if (plant_number != "" and plant_number != plant.plant_number) and (species_code != "" and species_code != species.species_code):
                self.add_error(None, "There is an mismatch between the given chemistry number, plant number, and species code.")
        except Chemistry.DoesNotExist:
            self.add_error('chemistry', 'Chemistry number does not match any known chemistry.')