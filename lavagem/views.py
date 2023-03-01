from django.shortcuts import render
from .models import Lavagem
from django.http import HttpResponse
# Create your views here.

def lavagem(request):
    if request.method == "GET":
        return render(request, 'lavagem.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        lavagem = Lavagem.objects.filter(email=email)
        if lavagem.exists():
            return render(request, 'lavagem.html', {'nome': nome, 'email': email, 'tel': tel})
        lavagem = Lavagem(
            nome=nome,
            email=email,
            tel=tel
        )

        lavagem.save()

        return  HttpResponse('Sua reserva confirmada!')

def agendados(request):
    if request.method == "GET":
        lavagem = Lavagem.objects.all()
        return render(request,'agendados.html',{'lavagem':lavagem})