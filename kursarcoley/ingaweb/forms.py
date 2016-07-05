from inga.models import Extraction, Chemistry, Plant, PlantSpecies
from django.forms import ModelForm

class ExtractionForm(ModelForm):
    class Meta:
        model = Extraction
        exclude = []