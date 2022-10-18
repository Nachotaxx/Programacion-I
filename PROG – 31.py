# Fecha: 13/10/22
# Autor: Ignacio Santos
#
"""
Desarrollar un programa que pida de a uno los nombres de los alumnos del curso (para terminar el ingreso se deberá
ingresar “Fin”). A medida que se ingresan, los nombres se irán agregando a una lista. Al finalizar el ingreso se deberá
imprimir la lista ordenada alfabéticamente y forzando los nombres completos a mayúsculas. Cada nombre deberá estar
precedido por el número de orden en 2 dígitos, por ejemplo:

        01 Ángel
        02 Carla
        03 Carlos
        ...
"""
listaNombres = []

while True:
    nombreAlumno = input("Ingrese nombre del alumno: ")
    if nombreAlumno == 'fin':
        break
    listaNombres.append(nombreAlumno)
    print(listaNombres)

listaNombres.sort()
print(listaNombres)

for i in range(0, len(listaNombres), 1):
    a = str(listaNombres[i])
    print(f"{i+1:02}...{a.capitalize()}")
