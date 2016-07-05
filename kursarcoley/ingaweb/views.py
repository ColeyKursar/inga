from django.shortcuts import render
from django.views.generic.edit import FormView
from ingaweb.forms import ExtractionForm

class ExtractionFormView(FormView):
    template_name = 'ingaweb/extraction_form.html'
    form_class = ExtractionForm
    success_url = '/recorded/'

    def form_valid(self, form):
        form.save()
        