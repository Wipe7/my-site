from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Tarefa
from .serializers import TarefaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar Tarefas
    
    Endpoints automáticos:
    - GET /api/tarefas/           - lista tarefas
    - POST /api/tarefas/          - cria tarefa
    - GET /api/tarefas/{id}/      - busca uma tarefa
    - PUT /api/tarefas/{id}/      - atualiza tarefa
    - PATCH /api/tarefas/{id}/    - atualiza parcial
    - DELETE /api/tarefas/{id}/   - deleta tarefa
    
    Endpoints customizados:
    - POST /api/tarefas/{id}/concluir/  - marca como concluída
    """
    
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        Retorna apenas as tarefas do usuário logado
        """
        return Tarefa.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        """
        Ao criar uma tarefa, associa ao usuário logado
        """
        serializer.save(usuario=self.request.user)
    
    @action(detail=True, methods=['post'])
    def concluir(self, request, pk=None):
        """
        Action customizada para marcar tarefa como concluída
        
        Uso: POST /api/tarefas/{id}/concluir/
        """
        tarefa = self.get_object()
        tarefa.concluida = True
        tarefa.save()
        
        serializer = self.get_serializer(tarefa)
        return Response({
            'mensagem': 'Tarefa concluída!',
            'tarefa': serializer.data
        })