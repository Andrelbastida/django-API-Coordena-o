# Este documento transforma toda a classe de Disciplina no estado de objeto para Json 
from rest_framework import serializers # Importa a biblioteca de serialização
from coordenacao.models.disciplinaModel import Disciplina# Importa o modelo Disciplina

class DisciplinaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Disciplina # Aqui, definimos que nosso modelo será DISCIPLINA
        fields = '__all__' # Este campo, define que todos os atributos de meu modelo, sejam serializados 