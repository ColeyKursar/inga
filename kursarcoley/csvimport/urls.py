from django.conf.urls import url
from csvimport.views import *


urlpatterns = [
    url(r'^csv/', SelectCSVView),
    url(r'^model.csv', GetCSVView),
]