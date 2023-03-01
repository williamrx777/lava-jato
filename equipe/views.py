from django.shortcuts import render

# Create your views here.

def equipe(request):
    if request.method == "GET":
        return render(request,'equipe.html')