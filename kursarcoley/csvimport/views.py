from django.shortcuts import render
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseBadRequest, HttpResponse
from django.apps import apps

# Create your views here.
def GetCSVView(request):
    if request.method != "GET":
        return HttpResponseBadRequest()

    print(request.POST)

    model_name = request.GET["model"].split(" ")[0]
    model = apps.get_model(app_label=settings.CSV_IMPORT_APPLICATION, model_name=model_name)
    field_objects = model._meta.get_fields()
    fields = []
    for field in field_objects:
        fields.append(field.name)

    return HttpResponse(",".join(fields))


def SelectCSVView(request):
    models = apps.get_app_config(settings.CSV_IMPORT_APPLICATION).get_models()
    context = { 'models': models }
    return render(request, 'csvimport/select.html', context)