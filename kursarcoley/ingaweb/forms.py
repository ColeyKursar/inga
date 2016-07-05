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
    plant = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    species = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dry_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    empty_vial_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    final_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    dry_marc_weight = forms.FloatField(disabled=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mass_extracted = forms.FloatField(disabled=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    proportion_remaining = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    percent_extracted = forms.FloatField(disabled=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    box = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))