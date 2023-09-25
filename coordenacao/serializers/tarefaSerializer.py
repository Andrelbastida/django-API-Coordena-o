# Este documento transforma toda a classe de tarefa de um objeto para Json 
from rest_framework import serializers  # Importa a biblioteca de serialização
from coordenacao.models.tarefaModel import Tarefa # Importa o modelo Tarefa

class TarefaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Tarefa # Aqui, definimos que nosso modelo será TAREFA
        fields = '__all__' # Este campo, define que todos os atributos de meu modelo, sejam serializados