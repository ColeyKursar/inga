from django.shortcuts import render
from django.http import HttpResponseRedirect
from ingaweb.forms import ExtractionForm
from inga.models import Extraction, Chemistry
from ingaweb.utilities import build_extraction, build_extraction_form

def ExtractionFormView(request):
    template = 'ingaweb/extraction_form.html'

    if request.method == 'POST':
        form = ExtractionForm(request.POST)
        
        if form.is_valid():
            extraction = build_extraction(form.cleaned_data)
            data = build_extraction_form(extraction)
            form = ExtractionForm(data)
        else:
            extraction = request.POST["extraction_number"]
            if extraction != "":
                try:
                    extraction = Extraction.objects.get(extraction_number = extraction)
                    data = build_extraction_form(extraction)
                    print(data)
                    form = ExtractionForm(data)
                except Extraction.DoesNotExist:
                    pass
    else: 
        form = ExtractionForm()
    
    return render(request, template, {'form': form})