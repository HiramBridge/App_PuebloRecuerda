from __future__ import unicode_literals

from django.db import models
from diputados.models import Diputado


# Create your models here.

class Iniciativa(models.Model):
    num = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    turno = models.TextField()
    comision = models.CharField(max_length=200)
    resolutivos = models.TextField()
    enlace = models.URLField()
    diputado = models.ForeignKey(Diputado,null=True,blank=True)

    def __unicode__(self):
        return '{} {}'.format(self.num, self.nombre)


