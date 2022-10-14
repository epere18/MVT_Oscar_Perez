from datetime import datetime
from random import random
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppCoder.models import Familiares
import random

def crear_personas(request, nombre, apellido):

    persona = Familiares(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_de_nacimiento=datetime.now())
    persona.save()

    template = loader.get_template("crear_personas.html")
    template_renderizado = template.render({"personas": persona})
    return HttpResponse(template_renderizado)

def ver_personas(request):

    personas = Familiares.objects.all()

    template = loader.get_template("ver_personas.html")
    template_renderizado = template.render({"personas": personas})
    return HttpResponse(template_renderizado)
