from django.conf.urls import url
from ingaweb.views import ExtractionFormView

urlpatterns = [
    url(r'^extraction/', ExtractionFormView.as_view()),
]
