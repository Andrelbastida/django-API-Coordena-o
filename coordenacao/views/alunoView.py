from rest_framework import generics
from coordenacao.models.alunoModel import Aluno
from coordenacao.serializers.alunoSerializer import AlunoSerializer



class AlunoListCreateView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer