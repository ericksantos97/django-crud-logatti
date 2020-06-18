from django.db import models


# Create your models here.
class Duvida(models.Model):
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20)
    data = models.CharField(max_length=20)
    nome_aluno = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao
