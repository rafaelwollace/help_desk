from django.contrib.auth.models import AbstractUser
from django.db import models
from setor.models import Setor
from unidade.models import Unidade


class User(AbstractUser):
    setor = models.ForeignKey(
        Setor, on_delete=models.CASCADE, blank=True, null=True)
    unidade = models.ForeignKey(
        Unidade, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True)
