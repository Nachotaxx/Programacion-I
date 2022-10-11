# Fecha: 11/10/22
# Autor: Ignacio Santos
#
"""
Se tiene la siguiente lista de temperaturas de los 31 días del mes de julio:
Temperaturas = [15 , 13.5 , 5.1 , 3 , 2.2 , -2 , -5 , 8 , 10 , 7.3 , 6 , 3.3 , 0 , -1 , 10 , 8.5 , 0 , 2 , -4 , -3.7 ,
 0 , 4.6 , 5 , 3 , -0.5 , 1 , 0 , -1 , 4 , 2.9 , -3.1 ]
Escribir un programa que modifique la lista reemplazando las temperaturas que son menores a 0 grados por la cadena “bajo
cero”. Imprimir por pantalla la lista modificada.
"""
#
Temperaturas = [15, 13.5, 5.1, 3, 2.2, -2, -5, 8, 10, 7.3, 6, 3.3, 0, -1, 10, 8.5,
                0, 2, -4, -3.7, 0, 4.6, 5, 3, -0.5, 1, 0, -1, 4, 2.9, -3.1]

for Temperaturas in Temperaturas:
    if Temperaturas < 0:
        print('Bajo cero')
    else:
        print(Temperaturas)

