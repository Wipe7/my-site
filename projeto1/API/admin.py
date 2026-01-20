from django.contrib import admin
from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'concluida', 'criado_em']
    list_filter = ['concluida', 'criado_em']
    search_fields = ['titulo', 'descricao']