# Autor: Ignacio Santos
# Fecha: 23/8/22
# Hacer un algoritmo que calcule cuántos kilómetros recorrerá un auto en ruta de acuerdo con
# la cantidad de litros de combustible ingresado
# Rendimiento:
# 14.1 km por litro
# Si tiene menos de 5 litros mostrar un mensaje para avisar que debe cargar combustible
#
# Pedir al usuario que ingrese la cantidad de litros de combustibles de su vehículo
litrosDeCombustible = input("Ingrese los litros de combustible: ")
#
# Cálculo de rendimiento para calcular la autonomy del vehículo
autonomia = float(litrosDeCombustible) * 14.1
print('La autonomia del vehiculo es:', autonomia)
#
# Condicional si el combustible es menor a 5 litros (mostrar mensaje de alerta)
# Inicio if
if float(litrosDeCombustible) <= 5:
    print('ATENCION COMBUSTIBLE BAJO!!!!! CARGUE COMBUSTIBLE ')
# Fin if

