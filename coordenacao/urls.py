from django.urls import path
#from  coordenacao.views.alunoView import AlunoDetailView, AlunoListCreateView
from coordenacao.views.alunoView import AlunoDetailView, AlunoListView
from  coordenacao.views.disciplinaView import DisciplinaListView , DisciplinaDetailView
from  coordenacao.views.tarefaView import TarefaDetailView, TarefaListView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoDetailView, basename='Alunos')
router.register('disciplinas', DisciplinaDetailView, basename='Disciplinas')
router.register('tarefas', TarefaDetailView, basename='Tarefas')


urlpatterns = [
    #path('alunos/', AlunoListCreateView.as_view(), name='aluno-list-create'), # para criar o Aluno você deve inserir a url local e adicionar “/api/alunos/” 
    path('alunos/', AlunoListView.as_view(), name='aluno-list-create'), # para criar o Aluno você deve inserir a url local e adicionar “/api/alunos/” 
    path('api/', include(router.urls)),
    path('alunos/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),# para deletar o Aluno você deve inserir a url local e adicionar “/api/alunos/ID_ALUNO” 
    path('disciplinas/', DisciplinaListView.as_view(), name='disciplina-list-create'),# para criar a Disciplina você deve inserir a url local e adicionar “/api/disciplina/”
    path('disciplinas/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),# para deletar a Disciplina você deve inserir a url local e adicionar “/api/disciplina/ID_Disciplina” 
    path('tarefas/', TarefaListView.as_view(), name='tarefa-list-create'),
    path('tarefas/<int:pk>/', TarefaDetailView.as_view(), name='tarefa-detail'),
]
