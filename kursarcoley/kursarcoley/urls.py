from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^web/', include("ingaweb.urls")),
    url(r'^update/', include("update.urls")),
    url(r'^api/', include("ingaapi.urls"))
]
