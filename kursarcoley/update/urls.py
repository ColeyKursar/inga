from django.conf.urls import url
from updater.views import UpdateView

urlpatterns = [
    url(r'^update/', UpdateView),
]
