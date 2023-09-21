# Este documento transforma toda a classe de aluno de um objeto para Json 
from rest_framework import serializers
from coordenacao.models.alunoModel import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'