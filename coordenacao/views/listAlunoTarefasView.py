from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from coordenacao.models.alunoModel import Aluno
from coordenacao.serializers.tarefaSerializer import TarefaSerializer

class ListAlunoTarefasView(APIView):
    def get(self, request, pk):
        try:
            aluno = Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        tarefas = aluno.tarefa_set.all()  # Obtém todas as tarefas associadas ao aluno
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)