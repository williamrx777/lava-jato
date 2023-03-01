from django.db import models

# Create your models here.

class Depoimento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome