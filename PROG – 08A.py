# Autor: Ignacio Santos
# Fecha: 25/8/22
#
'''Realizar un algoritmo que calcule la nota promedio de un curso. Se dispone de la nota de cada examen y
la cantidad de alumnos que lo rindieron. Utilizar el ciclo apropiado.'''
#
#

nota = float(input('Ingrese la nota del alumno: '))
acumuladorNotas = 0
contadorAlumnos = 0

while nota != 0 and nota <= 10:
    acumuladorNotas = acumuladorNotas + nota
    contadorAlumnos = contadorAlumnos + 1
    nota = float(input('Ingrese la nota del alumno: '))

# Calculo de nota promedio
notaPromedio = acumuladorNotas / contadorAlumnos
print('La nota promedio es: ', notaPromedio)





