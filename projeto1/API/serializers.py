from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    """Serializer para Tarefa"""
    
    usuario_nome = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'descricao', 'concluida', 'usuario', 'usuario_nome', 'criado_em']
        read_only_fields = ['id', 'usuario', 'criado_em']