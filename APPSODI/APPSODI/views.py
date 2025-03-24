from django.shortcuts import render, redirect
from django.http import HttpResponse

def mi_vista_principal(request):
    return render(request, 'pagina.html') # Renderiza tu plantilla HTML

def enlace1(request):
    return redirect("https://www.google.com") # Puedes cambiar esto por una plantilla o redirección

def enlace2(request):
    return redirect("https://www.google.com")

def enlace3(request):
    return redirect ("https://www.google.com")