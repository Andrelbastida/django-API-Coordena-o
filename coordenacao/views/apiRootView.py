from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from coordenacao.views.alunoView import AlunoListView
from coordenacao.views.disciplinaView import DisciplinaListView
from coordenacao.views.tarefaView import TarefaListView

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def api_root(request, format=None):
    return Response({
        'alunos': reverse('AlunoListView', request=request, format=format),
        'disciplinas': reverse('DisciplinaListView', request=request, format=format),
        'tarefas': reverse('TarefaListView', request=request, format=format),
    })
