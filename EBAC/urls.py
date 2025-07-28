from django.urls import path
from .views import post

urlpatterns = [
    path('', post, name='post'),  # ← aqui definimos a URL para a view 'post'
]
