# Este arquivo de URLs principal é onde você configura as URLs do seu projeto Django.

from django.contrib import admin
from django.urls import path, include
from coordenacao.urls import urlpatterns


urlpatterns = [
 #   path('admin/', admin.site.urls),
    path('api/', include('coordenacao.urls')),
]