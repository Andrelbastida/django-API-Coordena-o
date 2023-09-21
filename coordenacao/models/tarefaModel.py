from django.db import models
from coordenacao.models.alunoModel import Aluno  # Vamos importar a classe Aluno 
from coordenacao.models.disciplinaModel import Disciplina # Vamos importar a classe Disciplina

class Tarefa (models.Model):
    titulo = models.CharField(max_length=100)  # Cria um campo para inserir o titulo da tarefa com no máximo 100 Caracteres
    descricao = models.TextField() # Cria um campo para inserir a dercrição 
    data_entrega = models.DateField() # campo para a Data 
    concluida = models.BooleanField(default=False) # Cria um campo de confirmação se a tarefa foi concluida ? sim ou não 
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) # Campo para selecionar qual aluno está realizando a tarefa 
    disciplinas = models.ManyToManyField(Disciplina) # Campo para selecionar em qual disciplina está cadastrada

    def __str__(self): # retorna a classe no estado atual(objeto) como uma string
        return self.titulo