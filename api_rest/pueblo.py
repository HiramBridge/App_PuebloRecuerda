import requests

if __name__ == "pueblo":
    from sitiodb import ModeloDiputado
else:
    from api_rest.sitiodb import ModeloDiputado


class Ciudadano(object):

    def obten_Diputados(self):

        no_diputados = 0
        no_guardados = 0

        respuesta = requests.get("http://congresorest.appspot.com/diputado/")

        if respuesta.status_code == 200:
            datos_json = respuesta.json()

            for dato in datos_json:
                no_diputados += 1
                estado = ModeloDiputado.agregar(dato)

                if estado == 1:
                    estado_desc = "OK"
                    no_guardados += 1
                else:
                    estado_desc = "FAIL"

                print ("Guardando informacion de: {}......{}".format(
                    dato["nombre"],
                    estado_desc)
                )

        else:
            print ("Ocurrio errro al consumir WebService")


"""
Muestra de datos de diputados

{
    'tipo_de_eleccion': 'Mayoría Relativa',
    'cabecera': 'Jesús María',
    'email': 'pilar.moreno@congreso.gob.mx',
    'curul': 'A-009',
    'nu_diputado': '1',
    'entidad': 'Aguascalientes',
    'foto': 'None',
    'nombre': 'Moreno Montoya J. Pilar',
    'onomastico': '12-octubre',
    'fraccion': 'PRI',
    'suplente': ' Laura Patricia Romo Castorena',
    'distrito': '1'
}
"""
