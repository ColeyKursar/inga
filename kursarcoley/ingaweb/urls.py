from django.conf.urls import url
from ingaweb.views import *

urlpatterns = [
    url(r'^extraction/', ExtractionFormView),
    url(r'^batch/create/', BatchCreateView, name="BatchCreateView"),
    url(r'^batch/define/', BatchDefineView, name="BatchDefineView"),
    url(r'^batch/execute/', BatchExecuteView, name="BatchExecuteView")
]
