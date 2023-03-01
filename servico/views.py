from django.shortcuts import render

# Create your views here.

def servico(request):
    if request.method == "GET":
        return render(request, 'servico.html')