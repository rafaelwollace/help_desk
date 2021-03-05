from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from smart_selects.db_fields import ChainedForeignKey
from tipo_chamado.models import Sistema, TipoChamado

# Create your models here.


class Chamado(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    tipochamado = models.ForeignKey(TipoChamado, on_delete=models.CASCADE)
    sistema = ChainedForeignKey(
        Sistema,
        chained_field="tipochamado",
        chained_model_field="tipochamado",
        show_all=False,
        auto_choose=True,
        sort=True)
    descricao_chamado = models.TextField()
    data_chamado = models.DateField(blank=True, auto_now_add=True)
    hora_chamado = models.TimeField(blank=True, auto_now_add=True)
    arquivo_chamado = models.FileField(
        upload_to="arquivos/%Y/%m/", blank=True, null=True
    )
    tecnico_chamado = models.CharField(
        default="S",
        max_length=1,
        choices=(
            ("S", "selecione"),
            ("R", "Rafael W"),
            ("F", "Fernando M"),
            ("A", "André C"),
        ),
    )
    status_chamado = models.CharField(
        default="A",
        max_length=1,
        choices=(
            ("A", "Aberto"),
            ("R", "Reprovado"),
            ("E", "Encaminhado"),
            ("F", "Finalizado"),
        ),
    )

    def __str__(self):
        return f"{self.pk}"


class RespostaChamado(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE)
    resposta_autor = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    resposta_descricao = models.TextField()
    resposta_data = models.DateTimeField(default=now, blank=True)
    resposta_arquivo = models.FileField(
        upload_to="arquivos/%Y/%m/", blank=True, null=True
    )

    def __str__(self):
        return f"{self.chamado}"


class Meta:
    verbose_name = "Resposta Chamado"
    verbose_name_plural = "Respostas Chamados"
