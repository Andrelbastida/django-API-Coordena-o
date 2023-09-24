# # eclui o generics
# from rest_framework import generics
# #from rest_framework.views import APIView # estamos importando a biblioteca de API View
# from coordenacao.models.disciplinaModel import Disciplina
# from coordenacao.serializers.disciplinaSerializer import DisciplinaSerializer

# class DisciplinaListCreateView(generics.ListCreateAPIView):
#     queryset = Disciplina.objects.all()
#     serializer_class = DisciplinaSerializer

# class DisciplinaDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Disciplina.objects.all()
#     serializer_class = DisciplinaSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from coordenacao.models.disciplinaModel import Disciplina
from coordenacao.serializers.disciplinaSerializer import DisciplinaSerializer

# View para listar todas as disciplinas
class DisciplinaListView(APIView):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View para obter detalhes, atualizar e excluir uma disciplina específica
class DisciplinaDetailView(APIView):
    def get_object(self, pk):
        try:
            return Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        disciplina = self.get_object(pk)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    def put(self, request, pk):
        disciplina = self.get_object(pk)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        disciplina = self.get_object(pk)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
