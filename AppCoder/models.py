from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField(null=True)
