from datetime import datetime
from random import random
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppCoder.models import Familiares
import random

def index_personas(request):

    template = loader.get_template("index_personas.html")
    template_renderizado = template.render({})
    return HttpResponse(template_renderizado)


def crear_personas(request, nombre, apellido, edad):

    persona = Familiares(nombre=nombre, apellido=apellido, edad=edad, fecha_de_nacimiento=datetime.now())
    persona.save()

    template = loader.get_template("crear_personas.html")
    template_renderizado = template.render({"personas": persona})
    return HttpResponse(template_renderizado)

def ver_personas(request):

    personas = Familiares.objects.all()

    template = loader.get_template("ver_personas.html")
    template_renderizado = template.render({"personas": personas})
    return HttpResponse(template_renderizado)
