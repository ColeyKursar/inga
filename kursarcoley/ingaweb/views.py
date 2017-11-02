import csv
from io import TextIOWrapper
import json
from django.apps import apps
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from ingaweb.forms import ExtractionForm, BatchCreateForm, BatchDefineForm
from ingaweb.models import Batch
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
                    extraction = Extraction.objects.get(extraction_number=extraction)
                    data = build_extraction_form(extraction)
                    form = ExtractionForm(data)
                except Extraction.DoesNotExist:
                    pass
    else:
        form = ExtractionForm()

    return render(request, template, {'form': form})

def BatchExecuteView(request):
    if request.method == 'GET':
        return redirect('BatchCreateView')
    else:
        fields_to_ignore = ('', 'csrfmiddlewaretoken', 'batch', 'save')
        post = request.POST
        batch = Batch.objects.get(pk=post['batch'])

        mapping = {}


        for key, value in post.items():
            if key not in fields_to_ignore:
                mapping[key] = value

        batch.mapping = json.dumps(mapping)
        batch.save()

        errors = batch.process()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="errors.csv"'

        #headers = json.loads(batch.headers)

        batch.input_file.file.open('rt')
        csvfile = batch.input_file.file

        file = csv.DictReader(csvfile)

        writer = csv.DictWriter(response, file.fieldnames + ["error"])
        writer.writeheader()
        writer.writerows(errors)

        return response

def BatchDefineView(request):
    template = 'ingaweb/batch_define_form.html'

    if request.method == 'GET':
        return redirect('BatchCreateView')
    else:
        model = apps.get_app_config('inga').get_model(request.POST['table'])
        file = request.FILES['input_file']

        filewrapper = TextIOWrapper(file.file, encoding='utf8')
        csvdata = csv.DictReader(filewrapper)

        fields = model.names()
        headers = csvdata.fieldnames
        form = BatchDefineForm(fields, headers)

        batch = Batch()
        batch.headers = json.dumps(headers)
        batch.input_file = file
        batch.table = model.__name__
        batch.save()

        form.fields['batch'].initial = batch.id

    return render(request, template, {'form': form})


def BatchCreateView(request):
    template = 'ingaweb/batch_create_form.html'

    return render(request, template, {'form': BatchCreateForm()})
