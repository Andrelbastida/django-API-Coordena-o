# Este documento transforma toda a classe de Disciplina de um objeto para Json 
from rest_framework import serializers
from coordenacao.models.disciplinaModel import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'