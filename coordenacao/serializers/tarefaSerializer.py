# Este documento transforma toda a classe de tarefa de um objeto para Json 
from rest_framework import serializers
from coordenacao.models.tarefaModel import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'