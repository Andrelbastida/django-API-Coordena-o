from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from coordenacao.models.tarefaModel import Tarefa
from coordenacao.serializers.tarefaSerializer import TarefaSerializer

class TarefaListView(APIView):
    def get(self, request):
        # Método para listar todas as Tarefas (GET)
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many= True)
        return Response(serializer.data)

    def post(self, request):
        # Método para criar uma nova Tarefa (POST)\
        serializer = TarefaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # View para obter detalhes, atualizar e excluir uma tarefa específica
class TarefaDetailView(APIView):
    def get_object(self, pk):
        try:
            return Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

