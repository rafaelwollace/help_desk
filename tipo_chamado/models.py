from django.db import models

# Create your models here.


class TipoChamado(models.Model):
    nome_tipo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome_tipo}"


class Sistema(models.Model):
    tipochamado = models.ForeignKey(
        TipoChamado, on_delete=models.CASCADE)
    sistema_nome = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sistema_nome}"
