from __future__ import unicode_literals

from django.db import models


class Diputado(models.Model):
	nombre = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=50)
	pais= models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	fechaNacimiento= models.DateField()
	foto = models.ImageField(upload_to='/assets/images', null=True) 
	suplente= models.CharField(max_length=100)


