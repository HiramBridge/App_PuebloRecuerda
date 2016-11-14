# -*- coding: utf-8 -*-

# Librerias Python
import os
import sys

# Librerias Django
from django.db import connection
from django.core.wsgi import get_wsgi_application

print ("Programa que ejecuta: {}".format(__name__))

if __name__ == "sitiodb" or __name__ == "api_rest.sitiodb":
    project_abspath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

else:
    project_abspath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

print ("Ruta programa que ejecuta: {}".format(project_abspath))

"""
    La ruta correcta para ejecutar debiera ser algo como lo siguiente:
    /Users/Carlos/Files/Trabajo/Sintaxys/Proyectos/PuebloRecuerda/Sitio
"""

# Agregar path a las variables del sistema:
sys.path.append(project_abspath)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PuebloRecuerda.settings")

application = get_wsgi_application()


# Modelos
from diputados.models import Diputado


class ModeloDiputado(object):

    @classmethod
    def agregar(self, _datos):

        try:
            connection.close()
            diputado = Diputado(
                nombre=_datos["nombre"],
                email=_datos["email"],
                fechaNacimiento=_datos["onomastico"],
                suplente=_datos["suplente"]
            )
            diputado.save()

            return 1

        except Exception as e:
            print ("Error: {}".format(str(e)))
            return 0
