from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mi_vista_principal, name='principal'), # La página principal
    path('enlace1/', views.enlace1, name='enlace1'),
    path('enlace2/', views.enlace2, name='enlace2'),
    path('enlace3/', views.enlace3, name='enlace3'),
]