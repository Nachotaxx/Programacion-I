# Autor: Ignacio Santos
# Fecha: 23/8/22
# Hacer un algoritmo que calcule cuántos kilómetros recorrerá un auto en ruta de acuerdo con la cantidad de litros de
# combustible ingresados y el tipo de camino.
# Rendimiento:
# 14.1 km por litro en ruta
# 10.3 km por litro en ciudad
#
# Pedir al usuario que introduzca los litros de combustibles y el tipo de camino
litrosDeCombustible = input('Ingrese los litros de combustible: ')
tipoDeCamino = input('Ingrese el camino por el que manejara (ruta/ciudad): ')
#
# Condicional para calcular la autonomy en el tipo de camino elegido
if tipoDeCamino == 'ruta':
    autonomiaRuta = float(litrosDeCombustible) * 14.1
    print('La autonomia en ruta es:', autonomiaRuta
          )
else:
    autonoimiaCiudad = float(litrosDeCombustible) * 10.3
    print('La autonomia en ciudad es: ', autonoimiaCiudad
          )
