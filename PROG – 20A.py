# Autor: Ignacio Santos
# Fecha: 13/09/22
#
"""
Desarrollar un programa que pida un valor de hora, un valor de minuto, y un valor de segundo. A partir de esos valores
mostrar un reloj digital en formato de display HH:MM:SS (cada valor siempre en 2 dígitos). El display deberá avanzar
cada
1 segundo como cualquier reloj digital (es decir que cuando los segundos superen los 59 volverán a 00 y se agregará un
minuto, etc. Y lo mismo entre los minutos y las horas)
"""

"""
hora = 0
minutos = 0
segundos = 0

while True:
    hora = int(input('Ingrese la hora: '))
    minutos = int(input('Ingrese los minutos: '))
    segundos = int(input('Ingrese los segundos: '))

    if hora < 10:
        print("0")

    print(f'{hora}:')

    if minutos < 10:
        print("0")

    print(f'{minutos}:')

    if segundos < 10:
        print("0")

    print(f'{segundos}')

    # Aumentar en un segundo
    segundos = segundos + 1

    # Comprobar el tiempo
    if segundos == 60:
        minutos = minutos + 1
        segundos = 0

        if minutos == 60:
            hora = hora + 1
            minutos = 0

            if hora == 24:
                hora = 0

    # if segundos == 59:
    #     segundos = 00
    # elif minutos == 59:
    #     minutos = 00 + 1
    # elif hora == 12:
    #     hora = 00 + 1

    # print()
    # print(f'{hora}:{minutos}:{segundos}')
"""

# import time
#
# hora = int(input('Ingrese la hora: '))
# minutos = int(input('Ingrese los minutos: '))
# segundos = int(input('Ingrese los segundos: '))

"""
# Importar modulo
import time

# Obtencion de datos
hora = int(input("Ingrese un valor de hora: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))
# Programa
while hora < 24:
    while minutos <= 59:
        while segundos < 59:
            segundos = segundos + 1
            print(hora,":", minutos,":", segundos )
            time.sleep(0.25)
        segundos = 0
        print(hora,":", minutos,":", segundos )
        time.sleep(1)
        minutos = minutos + 1
    minutos = 0
    hora = hora + 1
    print(hora,":", minutos,":", segundos )
    time.sleep(1)
# + 23 horas
print("¡Ya pasaron 24 hs!")
"""

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Fecha: 27/09/22
# Ejercicio 20A escrito x mi


# Empezamos importando el módulo del tiempo
# Importar módulo
import time

# Datos al usuario
hora = int(input('Introduzca el valor de la hora: '))
minutos = int(input('Introduzca el valor en minutos: '))
segundos = int(input('Introduza los segundos: '))

# Programa(bucle)
while hora < 24:
    while minutos <= 59:
        while segundos < 59:
            segundos = segundos + 1
            print(f"{hora:02}:{minutos:02}:{segundos:02}")
            time.sleep(1)
        segundos = 0
        minutos = minutos + 1
        print(f"{hora:02}:{minutos:02}:{segundos:02}")
        time.sleep(1)
    minutos = 0
    hora = hora + 1
    print(f"{hora:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)
#
# Pero que pasa si el programa pasa las 24?
# le pongo que ha pasado un dia
print('Ha pasado 1 dia/ 24 horas')