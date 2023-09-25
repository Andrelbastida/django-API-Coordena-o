# Este documento transforma toda a classe de aluno no estado de objeto para Json 
from rest_framework import serializers # Importa a biblioteca de serialização
from coordenacao.models.alunoModel import Aluno # Importa o modelo Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno # Aqui, definimos que nosso modelo será o ALUNO 
        fields = '__all__' # Este campo, define que todos os atributos de meu modelo, sejam serializados 