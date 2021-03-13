from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from requests.api import request

from chamado import models
from chamado.models import Chamado


def index(request):
    chmdtotal = Chamado.objects.count()
    chmdaberto = Chamado.objects.filter(status_chamado='A').count()
    chmdfinalizado = Chamado.objects.filter(status_chamado='F').count()
    chamado = Chamado.objects.all()
    return render(request, 'principal/index.html', {
        'chamado': chamado,
        'chmdtotal': chmdtotal,
        'chmdaberto': chmdaberto,
        'chmdfinalizado': chmdfinalizado,
    })

    # Create your views here.
