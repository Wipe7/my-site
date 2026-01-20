from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Tarefa


class TarefaViewSetTest(APITestCase):
    """Testes para TarefaViewSet"""
    
    def setUp(self):
        """Configuração que roda antes de cada teste"""
        
        self.user1 = User.objects.create_user(
            username='user1',
            password='senha123'
        )
        
        self.user2 = User.objects.create_user(
            username='user2',
            password='senha123'
        )
        
        self.tarefa1 = Tarefa.objects.create(
            titulo='Tarefa do User 1',
            descricao='Fazer exercício',
            usuario=self.user1
        )
        
        self.tarefa2 = Tarefa.objects.create(
            titulo='Tarefa do User 2',
            descricao='Estudar Python',
            usuario=self.user2
        )
        
        self.client = APIClient()
    
    def test_listar_sem_autenticacao(self):
        """Teste 1: Usuário não autenticado não pode listar tarefas"""
        url = reverse('tarefa-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_listar_com_autenticacao(self):
        """Teste 2: Usuário autenticado pode listar suas tarefas"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('tarefa-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], 'Tarefa do User 1')
    
    def test_usuario_nao_ve_tarefa_de_outro(self):
        """Teste 3: User1 não pode ver tarefas do User2"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('tarefa-list')
        response = self.client.get(url)
        
        self.assertEqual(len(response.data), 1)
        titulos = [t['titulo'] for t in response.data]
        self.assertNotIn('Tarefa do User 2', titulos)
    
    def test_criar_tarefa(self):
        """Teste 4: Criar nova tarefa"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('tarefa-list')
        data = {
            'titulo': 'Nova Tarefa',
            'descricao': 'Fazer testes unitários'
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarefa.objects.count(), 3)
        
        nova_tarefa = Tarefa.objects.get(titulo='Nova Tarefa')
        self.assertEqual(nova_tarefa.usuario, self.user1)
        self.assertFalse(nova_tarefa.concluida)
    
    def test_atualizar_tarefa(self):
        """Teste 5: Atualizar tarefa existente"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('tarefa-detail', kwargs={'pk': self.tarefa1.pk})
        data = {
            'titulo': 'Tarefa Atualizada',
            'descricao': 'Descrição nova'
        }
        
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tarefa1.refresh_from_db()
        self.assertEqual(self.tarefa1.titulo, 'Tarefa Atualizada')
        self.assertEqual(self.tarefa1.descricao, 'Descrição nova')
    
    def test_deletar_tarefa(self):
        """Teste 6: Deletar tarefa"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('tarefa-detail', kwargs={'pk': self.tarefa1.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tarefa.objects.count(), 1)
    
    def test_concluir_tarefa(self):
        """Teste 7: Action customizada - concluir tarefa"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('tarefa-concluir', kwargs={'pk': self.tarefa1.pk})
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tarefa1.refresh_from_db()
        self.assertTrue(self.tarefa1.concluida)
        self.assertIn('mensagem', response.data)
        self.assertEqual(response.data['mensagem'], 'Tarefa concluída!')