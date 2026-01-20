from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TarefaViewSet

# Criar o router
router = DefaultRouter()

# Registrar a ViewSet
router.register(r'tarefas', TarefaViewSet, basename='tarefa')

# URLs
urlpatterns = [
    path('', include(router.urls)),
]