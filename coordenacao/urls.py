from django.urls import path
from  coordenacao.views.alunoView import AlunoDetailView, AlunoListCreateView
from  coordenacao.views.disciplinaView import DisciplinaListCreateView , DisciplinaDetailView
from  coordenacao.views.tarefaView import TarefaDetailView, TarefaListCreateView

urlpatterns = [
    path('alunos/', AlunoListCreateView.as_view(), name='aluno-list-create'), # para criar o Aluno você deve inserir a url local e adicionar “/api/alunos/” 
    path('alunos/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),# para deletar o Aluno você deve inserir a url local e adicionar “/api/alunos/ID_ALUNO” 
    path('disciplinas/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),# para criar a Disciplina você deve inserir a url local e adicionar “/api/disciplina/”
    path('disciplinas/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),# para deletar a Disciplina você deve inserir a url local e adicionar “/api/disciplina/ID_Disciplina” 
    path('tarefas/', TarefaListCreateView.as_view(), name='tarefa-list-create'),
    path('tarefas/<int:pk>/', TarefaDetailView.as_view(), name='tarefa-detail'),
]
