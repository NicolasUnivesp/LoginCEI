from django.db import models


class Livros(models.Model):
    objects = models.Manager()
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    ano = models.IntegerField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    disponivel = models.BooleanField(blank=True, null=True)
