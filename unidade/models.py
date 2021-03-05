from django.db import models

# Create your models here.


class Unidade(models.Model):
    nome_unidade = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.nome.unidade}'
