from django.shortcuts import render, redirect
from django.http import HttpResponse

def mi_vista_principal(request):
    return render(request, 'pagina.html')

def enlace1(request):
    return redirect("https://apps.apple.com/cl/app/sodimac-casa-y-construcci%C3%B3n/id532353705?mt=8") 

def enlace2(request):
    return render(request, 'link.html',)

def enlace3(request):
    return redirect ("https://www.circulodeespecialistas.cl/activaciones-en-tienda?tienda=90")

def enlace4(request):
    return redirect("https://www.bancofalabella.cl/pre-landing?utm_source=Sodimac&utm_medium=QRregional&utm_content=belloto-qr-unificado&utm_campaign=apertura-sodimac&utm_term=259303483&store_id=90")

def enlace5(request):
    return redirect("https://www.bancofalabella.cl/pre-landing?utm_source=Sodimac&utm_medium=QRregional&utm_content=belloto-qr-unificado&utm_campaign=apertura-sodimac&utm_term=259303483&store_id=90")

def enlace7(request):
    return redirect("https://www.bancofalabella.cl/pre-landing?utm_source=Sodimac&utm_medium=QRregional&utm_content=belloto-qr-unificado&utm_campaign=apertura-sodimac&utm_term=259303483&store_id=90")