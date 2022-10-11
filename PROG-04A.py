# Autor: Ignacio Santos
# Fecha: 23/8/22
# Realizar un programa que permita ingresar la cantidad de inscriptos a
# una conferencia y la cantidad de asientos disponibles
# en el auditorio. Se debe indicar si alcanzan los asientos. Si los
# asientos no alcanzan, indicar cuantos faltan para que todos
# los inscriptos puedan sentarse.
#
cantidadDeInscriptos = input('Ingrese la cantidad de inscriptos: ')
cantidadDeAsientos = input('Ingrese la cantidad de asientos: ')
print()
#
if cantidadDeAsientos == cantidadDeInscriptos:
    print('La cantidad de asientos es suficiente ')
elif cantidadDeInscriptos > cantidadDeAsientos:
    print('Los asientos no alcanzan ')
    asientosFaltantes = int(cantidadDeInscriptos) - int(cantidadDeAsientos)
    print('Los asientos que faltan son: ', asientosFaltantes)
else:
    print('Los asientos no alcanzan ')
    asientosFaltantes = int(cantidadDeInscriptos) - int(cantidadDeAsientos)
    print('Los asientos que faltan son: ', asientosFaltantes)
#
