from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import Categoria, Tarefa, Comentario
from .serializers import (
    CategoriaSerializer, 
    TarefaSerializer,
    ComentarioSerializer
)


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar Categorias
    
    Esta ViewSet fornece automaticamente:
    - GET /api/categorias/          -> lista todas
    - POST /api/categorias/         -> cria nova
    - GET /api/categorias/{id}/     -> busca uma específica
    - PUT /api/categorias/{id}/     -> atualiza completa
    - PATCH /api/categorias/{id}/   -> atualiza parcial
    - DELETE /api/categorias/{id}/  -> deleta
    """
    
    # 1. Define quais objetos serão gerenciados
    queryset = Categoria.objects.all()
    
    # 2. Define qual serializer será usado
    serializer_class = CategoriaSerializer
    
    # 3. Define quem pode acessar (apenas autenticados)
    permission_classes = [IsAuthenticated]