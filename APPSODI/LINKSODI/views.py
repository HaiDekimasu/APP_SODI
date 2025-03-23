from django.shortcuts import render
from django.http import HttpResponse

def mi_vista_principal(request):
    return render(request, 'pagina.html') # Renderiza tu plantilla HTML

def enlace1(request):
    return HttpResponse("¡Este es el enlace 1!") # Puedes cambiar esto por una plantilla o redirección

def enlace2(request):
    return HttpResponse("¡Este es el enlace 2!")

def enlace3(request):
    return HttpResponse("¡Este es el enlace 3!")