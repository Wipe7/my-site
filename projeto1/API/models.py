from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    """Modelo  de Tarefa"""
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-criado_em']
    
    def __str__(self):
        return self.titulo