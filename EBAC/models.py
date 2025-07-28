from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nome} ({self.disciplina})"
