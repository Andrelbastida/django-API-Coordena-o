from rest_framework import generics
from coordenacao.models.tarefaModel import Tarefa
from coordenacao.serializers.tarefaSerializer import TarefaSerializer


class TarefaListCreateView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer