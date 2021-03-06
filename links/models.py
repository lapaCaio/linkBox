from django.db import models

from pages.models import Page

class Link(models.Model):
    titulo = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    data_criacao = models.DateTimeField("Data de Criação", auto_now_add=True)
    data_atualizacao = models.DateTimeField("Data de Atualização", auto_now=True)
    link_ativo = models.BooleanField(default=True)
    ordem_link = models.PositiveIntegerField("Ordem do Links", null=True, blank=True)
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo 