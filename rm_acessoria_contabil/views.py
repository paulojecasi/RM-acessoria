from django.shortcuts import render
from .models import TextoSite
# Create your views here.

def acessoriaContabil(request):

    textosDoSite = TextoSite.objects.all()

    dados = {
       'TextosDoSite': textosDoSite}

    return render(request,'index.html',dados)

