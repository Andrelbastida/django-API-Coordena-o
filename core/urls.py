# Este arquivo de URLs principal é onde você configura as URLs do seu projeto Django.

from django.contrib import admin
from django.urls import path, include
from coordenacao.urls import urlpatterns
#from coordenacao.views.alunoView import AlunoListCreateView


#from rest_framework import routers # estou importando a biblioteca para exibir as rotas da nossa API 

# router = routers.DefaultRouter()
# router.register('alunos', AlunoListCreateView, basename='Alunos' )

urlpatterns = [
 #   path('admin/', admin.site.urls),
    #path('', include(router.urls)), ### corrigir depois 
    path('api/', include('coordenacao.urls')),
]