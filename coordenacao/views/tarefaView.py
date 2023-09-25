from rest_framework.views import APIView # estamos importando a biblioteca de API View.
from rest_framework.response import Response # Importa a classe Response para enviar respostas HTTP.
from rest_framework import status # Importa códigos de status HTTP.

from coordenacao.models.tarefaModel import Tarefa # Importa o modelo Tarefa
from coordenacao.serializers.tarefaSerializer import TarefaSerializer # Importa o serializador TarefaSerializer 

class TarefaListView(APIView): # View para listar todas as tarefas e adicionar alguma tarefa
    def get(self, request): # Método para listar todas as Tarefas (GET)
        tarefas = Tarefa.objects.all()# Consulta todas as tarefas
        serializer = TarefaSerializer(tarefas, many= True)# Serializa a lista de tarefas
        return Response(serializer.data) # Retorna os dados serializados das tarefas como resposta HTTP

    def post(self, request):# Método para criar uma nova Tarefa (POST)
        serializer = TarefaSerializer(data= request.data) # Serializa os dados recebidos na requisição
        if serializer.is_valid(): # Verifica se os dados serializados são válidos
            serializer.save() # Salva a nova tarefa no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna os dados da tarefa criada com status 201 (Created)
        #Caso apresente algum erro :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Retorna os erros de validação com status 400 (Bad Request)
        
    
class TarefaDetailView(APIView):# View para obter detalhes, atualizar e excluir uma tarefa específica
    def get_object(self, pk): # Função auxiliar para obter uma tarefa com base no ID (GET).
        try:
            return Tarefa.objects.get(pk=pk) # Tenta obter a tarefa com o ID fornecido (Primary Key = ID).
        except Tarefa.DoesNotExist: # Se a tarefa não existir:
            raise status.HTTP_404_NOT_FOUND # Retorna um erro Http404 para indicar que a tarefa não foi encontrada

    def get(self, request, pk): # Método para obter detalhes de uma tarefa específica através de seu ID (GET).
        tarefa = self.get_object(pk) # Obtém a tarefa com base no ID fornecido (Primary Key = ID).
        serializer = TarefaSerializer(tarefa)  # Serializa os atributos da tarefa
        return Response(serializer.data) # Retorna os atributos da tarefa como resposta.

    def put(self, request, pk): # Método para atualizar os atributos de uma tarefa específica (PUT).
        tarefa = self.get_object(pk) # Obtém a tarefa com base no ID fornecido (Primary Key = ID).
        serializer = TarefaSerializer(tarefa, data=request.data) # Serializa os dados ATUALIZADOS da tarefa
        if serializer.is_valid(): # Verifica se os dados serializados são válidos
            serializer.save() # Salva as atualizações da tarefa no banco de dados
            return Response(serializer.data) # Retorna os dados atualizados da tarefa como resposta HTTP
        #Caso apresente algum erro :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Retorna os erros de validação com status 400 (Bad Request)

    def delete(self, request, pk): # Método para excluir uma tarefa específica (DELETE).
        tarefa = self.get_object(pk) # Obtém a tarefa com base no ID fornecido (Primary Key = ID).
        tarefa.delete() # Exclui a tarefa do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT) # Retorna uma resposta vazia com status 204 (No Content)

