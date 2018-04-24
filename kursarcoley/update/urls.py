from django.conf.urls import url
from update.views import UpdateView

urlpatterns = [
    url(r'^update/', UpdateView),
]
