from django.db import models

class Aluno (models.Model):
    nome = models.CharField(max_length=100) # Cria um campo para inserir o nome do aluno com no máximo 100 Caracteres
    email = models.EmailField(unique=True) # Cria um campo para inserir o e-mail e verifica se ele é unico 

    def __str__(self):  # retorna a classe no estado atual(objeto) como uma string
        return self.nome