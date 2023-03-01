from django.db import models
# Create your models here.

class Lavagem(models.Model):
    nome = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome