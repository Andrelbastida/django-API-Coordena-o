from rest_framework.views import APIView # estamos importando a biblioteca de API View.
from rest_framework.response import Response # Importa a classe Response para enviar respostas HTTP.
from rest_framework import status # Importa códigos de status HTTP.

from coordenacao.models.alunoModel import Aluno # Importa o modelo Aluno.
from coordenacao.serializers.alunoSerializer import AlunoSerializer # Importa o serializador AlunoSerializer.


class AlunoListView(APIView): # View para listar todos os alunos adicionar algum
    def get(self, request): # Método para listar todos os alunos (GET).
        alunos = Aluno.objects.all() # Consulta todos os Alunos 
        serializer = AlunoSerializer(alunos, many=True) # Serializa a lista com todos os alunos
        return Response(serializer.data) # Retorna todos os alunos serializados. 

    def post(self, request): # Método para criar um novo aluno (POST)
        serializer = AlunoSerializer(data=request.data) # Serializa os dados depositados
        if serializer.is_valid(): # Verifica se são dados válidos
            serializer.save() # Salva o novo aluno 
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna os dados do novo aluno com status 201(Criado)
        #Caso apresente algum erro :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Retorna os erros de validação com status 400 (Bad Request)


class AlunoDetailView(APIView): # View para obter, atualizar e excluir um aluno específico
    def get_object(self, pk): # Função auxiliar para obter um aluno com base no ID
        try:
            return Aluno.objects.get(pk=pk) # Tenta obter o aluno com o ID fornecido
        except Aluno.DoesNotExist: # Caso o aluno não exista:
            raise status.HTTP_404_NOT_FOUND # Retorna um erro Http404 para indicar que o aluno não foi encontrado


    def get(self, request, pk): # Método para obter detalhes de um aluno específico através de seu ID (GET).
        aluno = self.get_object(pk) # Obtém o aluno com base no ID fornecido (Primary Key = ID).
        serializer = AlunoSerializer(aluno) # Serializa os atributos do aluno.
        return Response(serializer.data) # Retorna com os atributos do aluno.

    def put(self, request, pk): # Método para atualizar os atributos de um aluno específico (PUT).
        aluno = self.get_object(pk) # Obtém o aluno com base no ID fornecido (Primary Key = ID).
        serializer = AlunoSerializer(aluno, data=request.data) # Serializa os atributos ATUALIZADOS do aluno.
        if serializer.is_valid(): # Verifica se são dados válidos
            serializer.save() # Salva os atributos atualizados
            return Response(serializer.data) # Retorna uma resposta HTTP com os atributos do aluno já atualizados.
        #Caso apresente algum erro :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Retorna os erros de validação com status 400 (Bad Request)



    def delete(self, request, pk): # Método para excluir um aluno específico (DELETE).
        aluno = self.get_object(pk) # Obtém o aluno com base no ID fornecido (Primary Key = ID).
        aluno.delete() # Exclui o aluno do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT)  # Retorna uma HTTP vazia com status 204 (No Content)

    