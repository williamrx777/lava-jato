from django.shortcuts import render
from .models import Depoimento
# Create your views here.

def depoimento(request):
    if request.method == "GET":
        depoimento = Depoimento.objects.all()
        return render(request,'depoimento.html',{'depoimento':depoimento})