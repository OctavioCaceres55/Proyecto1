from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
import datetime
from django.template import loader

def probandoTemplate(self):
    nom = "Juan"
    ap = "Perez"
    listaDeNotas = [2,4,2,5,6,9,10,5]
    dic = {"nombre": nom, "hoy":datetime.datetime.now(), "apellido": ap, "notas": listaDeNotas}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(dic)

    return HttpResponse(documento)




