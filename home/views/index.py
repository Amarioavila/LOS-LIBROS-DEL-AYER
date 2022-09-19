from contextvars import Context
from datetime import datetime
import http
from pipes import Template
from re import template
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Template, Context

def homepage(request):
    return HttpResponse("hola Mundo!!")

def plantilla1(request):
    suma = 10+3
    fecha = datetime.now()
    lista1 =[1,2,3,4,5]
    lista2 =["camilo", "Andres", "Brian", "jaime"]
    
    Plan_exter = open(r"C:\Users\jeanp\OneDrive\Escritorio\Proyecto\LosLibrosDelAyer\home\templates\base.html") #aqui abrimos la plantilla
    plantilla = Template(Plan_exter.read()) #Con esto vamos a leer la plantilla (cargar plantilla)
    Plan_exter.close()
    contexto = Context({"A":suma,"B":fecha,"lista1":lista1,"lista2":lista2})
    Documento = plantilla.render(contexto) #Pasa de html a http
    return HttpResponse(Documento)