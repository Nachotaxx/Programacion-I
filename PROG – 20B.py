# Fecha: 27/09/22
# Autor: Ignacio Santos
#

""""
# Importar módulo
import time
#
# Datos al usuario
hora = int(input('Introduzca el valor de la hora: '))
minutos = int(input('Introduzca el valor en minutos: '))
segundos = int(input('Introduza los segundos: '))


# Programa Principal
while hora < 24:
    while minutos <= 59:
        while segundos < 59:
            print(f"{hora:02}:{minutos:02}:{segundos:02}")
            segundos = segundos - 1
            time.sleep(.20)
        if hora == 0 and minutos == 0 and segundos == 0:
            print(f"{hora:02}:{minutos:02}:{segundos:02}")
            print('El programa termino')
            exit()
        print(f"{hora:02}:{minutos:02}:{segundos:02}")
        segundos = 59
        minutos = minutos - 1
        time.sleep(1)

    print(f"{hora:02}:{minutos:02}:{segundos:02}")
    hora = hora - 1
    minutos = 59
    time.sleep(1)
"""
#
#
print("<<<< TIEMPO >>>>")

"""
# Importar modulo
import time
# Obtencion de datos
hora = int(input("Ingrese un valor de hora: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))
# Progama
while hora >= 0:
    while minutos >= 0:
        while segundos > 0:
            print(f"{hora:02}:{minutos:02}:{segundos:02}")
            segundos = segundos - 1
            time.sleep(1)
        # Si llega a 0 terminar
        if hora == 0 and minutos == 0 and segundos == 0:
            print(f"{hora:02}:{minutos:02}:{segundos:02}")
            print("¡Ya termino el tiempo!")
            exit()
        print(f"{hora:02}:{minutos:02}:{segundos:02}")
        time.sleep(1)
        minutos = minutos - 1
        segundos = 59
    hora = hora - 1
    minutos = 59
    print(f"{hora:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)
"""

# Importar módulo
import time

# Datos al usuario
hora = int(input('Introduzca el valor de la hora: '))
minutos = int(input('Introduzca el valor en minutos: '))
segundos = int(input('Introduza los segundos: '))

# Programa principal
while hora >= 0:
    while minutos >= 0:
        while segundos > 0:
            print(f"{hora:02}:{minutos:02}:{segundos:02}")
            segundos = segundos - 1
            time.sleep(.2)
        if hora == 0 and minutos == 0 and segundos == 0:
            print(f"{hora:02}:{minutos:02}:{segundos:02}")
            print("Ya termino el timpo")
            exit()
        print(f"{hora:02}:{minutos:02}:{segundos:02}")
        minutos = minutos - 1
        segundos = 59
        time.sleep(1)
    print(f"{hora:02}:{minutos:02}:{segundos:02}")
    hora = hora - 1
    minutos = 59
    time.sleep(1)
# Fin programa



