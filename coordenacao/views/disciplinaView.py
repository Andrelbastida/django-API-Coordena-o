from rest_framework.views import APIView # estamos importando a biblioteca de API View.
from rest_framework.response import Response # Importa a classe Response para enviar respostas HTTP.
from rest_framework import status # Importa códigos de status HTTP.

from coordenacao.models.disciplinaModel import Disciplina  # Importa o modelo Disciplina 
from coordenacao.serializers.disciplinaSerializer import DisciplinaSerializer  # Importa o serializador DisciplinaSerializer 


class DisciplinaListView(APIView): # View para listar todas as disciplinas e adicionar alguma disciplina
    def get(self, request): # Método para listar todas as Disciplinas (GET)
        disciplinas = Disciplina.objects.all()  # Consulta todas as disciplinas
        serializer = DisciplinaSerializer(disciplinas, many=True)  # Serializa a lista de disciplinas
        return Response(serializer.data) # Retorna os dados serializados das disciplinas como resposta HTTP

    def post(self, request): # Método para criar uma nova disciplina (POST)
        serializer = DisciplinaSerializer(data=request.data) # Serializa os dados recebidos na requisição
        if serializer.is_valid():  # Verifica se os dados serializados são válidos
            serializer.save() # Salva a nova disciplina no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna os dados da disciplina criada com status 201 (Created)
        #Caso apresente algum erro :    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna os erros de validação com status 400 (Bad Request)


class DisciplinaDetailView(APIView):# View para obter, atualizar e excluir uma disciplina específica
    def get_object(self, pk): # Função auxiliar para obter uma disciplina com base no ID (GET).
        try:
            return Disciplina.objects.get(pk=pk) # Tenta obter a disciplina com o ID fornecido (Primary Key = ID).
        except Disciplina.DoesNotExist:  # Se a disciplina não existir:
            raise status.HTTP_404_NOT_FOUND  # Retorna um erro Http404 para indicar que a disciplina não foi encontrada

    def get(self, request, pk): # Método para obter detalhes de uma disciplina específica através de seu ID (GET).
        disciplina = self.get_object(pk)  # Obtém a disciplina com base no ID fornecido (Primary Key = ID).
        serializer = DisciplinaSerializer(disciplina)  # Serializa os atributos da disciplina 
        return Response(serializer.data)  # Retorna os atributos da disciplina como resposta.

    def put(self, request, pk): # Método para atualizar os atributos de uma disciplina específica (PUT).
        disciplina = self.get_object(pk)  # Obtém a disciplina com base no ID fornecido (Primary Key = ID).
        serializer = DisciplinaSerializer(disciplina, data=request.data) # Serializa os dados ATUALIZADOS da disciplina
        if serializer.is_valid():  # Verifica se os dados serializados são válidos
            serializer.save()  # Salva as atualizações da disciplina no banco de dados
            return Response(serializer.data) # Retorna os dados atualizados da disciplina como resposta HTTP
        #Caso apresente algum erro :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Retorna os erros de validação com status 400 (Bad Request)

    def delete(self, request, pk): # Método para excluir uma disciplina específica (DELETE).
        disciplina = self.get_object(pk) # Obtém a disciplina com base no ID fornecido (Primary Key = ID).
        disciplina.delete()  # Exclui a disciplina do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT) # Retorna uma resposta vazia com status 204 (No Content)
