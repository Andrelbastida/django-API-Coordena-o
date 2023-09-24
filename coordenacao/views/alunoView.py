# eclui o generics
from rest_framework.views import APIView # estamos importando a biblioteca de API View
from coordenacao.models.alunoModel import Aluno
from coordenacao.serializers.alunoSerializer import AlunoSerializer
from rest_framework.response import Response

class AlunoListView(APIView):
    def get(self, request):
        # Método para listar todos os alunos (GET)
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Método para criar um novo aluno (POST)
        form = AlunoForm(request.data)
        if form.is_valid():
            nome = form.cleaned_data['nome']  
            email = form.cleaned_data['email']
            aluno = Aluno(nome=nome, email=email)
            aluno.save()
            serializer = AlunoSerializer(aluno)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class AlunoDetailView(APIView):
    def get(self, request, pk):
        # Método para obter detalhes de um aluno específico (GET)
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, pk):
        # Método para atualizar os detalhes de um aluno específico (PUT)
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
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