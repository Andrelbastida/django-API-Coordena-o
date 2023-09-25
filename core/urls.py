from django.contrib import admin
from django.urls import path, include
from coordenacao.urls import urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls), # Define a rota para a interface de administração do Django
    path('api/', include('coordenacao.urls')),  # Define a rota para as URLs do aplicativo 'coordenacao' usando 'include', para adiciona-las 
]