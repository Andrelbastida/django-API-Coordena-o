from rest_framework import generics
from coordenacao.models.disciplinaModel import Disciplina
from coordenacao.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaListCreateView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer