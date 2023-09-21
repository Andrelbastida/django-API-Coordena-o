from django.db import models

class Disciplina (models.Model):
    nome = models.CharField(max_length=100) # Cria um campo para inserir o nome do aluno com no máximo 100 Caracteres
    descricao = models.TextField() # Cria um campo para inserir a descrição 

    def __str__(self): # retorna a classe no estado atual(objeto) como uma string
        return self.nome