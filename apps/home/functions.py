import datetime
from .models import *

def comprobar_disponibilidad(departamento, fecha_ingreso, fecha_salida):
    lista_disponibilidad =[]
    reserva_list = RESERVA.objects.filter(RES_DEPARTAMENTO=departamento)
    for reserva in reserva_list:
        if reserva.RES_FECHA_INGRESO > fecha_salida or reserva.RES_FECHA_SALIDA < fecha_ingreso:
            lista_disponibilidad.append(True)
        else:
            lista_disponibilidad.append(False)

    return all(lista_disponibilidad)