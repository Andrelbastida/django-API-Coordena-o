from django.urls import path
from coordenacao.views.alunoView import AlunoDetailView, AlunoListView
from  coordenacao.views.disciplinaView import DisciplinaListView , DisciplinaDetailView
from  coordenacao.views.tarefaView import TarefaDetailView, TarefaListView
from coordenacao.views.listAlunoTarefasView import ListAlunoTarefasView


urlpatterns = [
    path('alunos/', AlunoListView.as_view(), name='aluno-list-create'), # Endereço para listar todos os Alunos, você deve inserir a url local e adicionar “/api/alunos/”
    path('alunos/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),# Endereço para buscar, alterar ou deletar o Aluno, você deve inserir a url local e adicionar “/api/alunos/ID_ALUNO/” 
    path('disciplinas/', DisciplinaListView.as_view(), name='disciplina-list-create'),# Endereço para listar todas as Disciplinas, você deve inserir a url local e adicionar “/api/disciplina/”
    path('disciplinas/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),# Endereço para buscar, alterar ou deletar a Disciplina, você deve inserir a url local e adicionar “/api/disciplina/ID_Disciplina/” 
    path('tarefas/', TarefaListView.as_view(), name='tarefa-list-create'), # Endereço para listar todas as Tarefas, você deve inserir a url local e adicionar “/api/tarefas/”
    path('tarefas/<int:pk>/', TarefaDetailView.as_view(), name='tarefa-detail'), # Endereço para buscar, alterar ou deletar a Tarefa, você deve inserir a url local e adicionar “/api/tarefas/ID_TAREFA/” 
    path('alunos/<int:pk>/tarefas/', ListAlunoTarefasView.as_view(), name='list-aluno-tarefas'), # Endereço para listar todas as tarefas de um determinado aluno, você deve inserir a url local e adicionar “/api/alunos/ID_ALUNO/tarefas/”
    
]
