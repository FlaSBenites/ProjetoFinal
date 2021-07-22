from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    mensagem = models.CharField(max_length=200)
    email = models.EmailField()
    novidades = models.BooleanField()

    def __str__(self):
        return self.nome