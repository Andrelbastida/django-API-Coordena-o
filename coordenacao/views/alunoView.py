from rest_framework.views import APIView # estamos importando a biblioteca de API View.
from rest_framework.response import Response # Importa a classe Response para enviar respostas HTTP.
from rest_framework import status # Importa códigos de status HTTP.

from coordenacao.models.alunoModel import Aluno # Importa o modelo Aluno.
from coordenacao.serializers.alunoSerializer import AlunoSerializer # Importa o serializador AlunoSerializer.


class AlunoListView(APIView): # Método para listar todos os alunos (GET).
    def get(self, request):
        alunos = Aluno.objects.all() # Obtemos todos os atributos de nosso modelo Aluno e resumimos como "alunos". 
        serializer = AlunoSerializer(alunos, many=True) # Serializa os atributos de nosso modelo.
        return Response(serializer.data) # Retorna os atributos serializados. 

    def post(self, request): # Método para criar um novo aluno (POST)
        serializer = AlunoSerializer(data=request.data) # Serializa os dados depositados
        if serializer.is_valid(): # Verifica se são dados válidos
            serializer.save() # Salva o novo aluno 
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna os dados do novo aluno com status 201(Criado)
        #Caso apresente algum erro :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Retorna os erros de validação com status 400 (Bad Request)

class AlunoDetailView(APIView): 
    def get(self, request, pk): # Método para obter detalhes de um aluno específico através de seu ID (GET).
        aluno = self.get_object(pk) # Obtém o aluno com base no ID fornecido.
        serializer = AlunoSerializer(aluno) # Serializa os atributos do aluno.
        return Response(serializer.data) # Retorna os atributos do aluno como resposta HTTP.

    def put(self, request, pk): # Método para atualizar os atributos de um aluno específico (PUT).
        aluno = self.get_object(pk) # Obtém o aluno com base no ID fornecido
        serializer = AlunoSerializer(aluno, data=request.data) # Serializa os atributos ATUALIZADOS do aluno.
        if serializer.is_valid(): # Verifica se são válidos
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        # Método para atualizar parcialmente os detalhes de um aluno específico (PATCH)
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Método para excluir um aluno específico (DELETE)
        aluno = self.get_object(pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        # Função auxiliar para obter um aluno com base no ID
        try:
            return Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND