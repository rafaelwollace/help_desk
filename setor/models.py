from django.db import models

# Create your models here.


class Setor(models.Model):
    nome_setor = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.nome_setor}'
