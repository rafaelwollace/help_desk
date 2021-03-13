from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from chamado.models import Chamado
from . import models


class ListaChamados(View):
    model = models.Chamado


class DetalheChamados(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhes')
    # Create your views here.
