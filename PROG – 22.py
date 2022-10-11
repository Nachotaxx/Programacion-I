# Fecha: 4/10/22
# Autor: Ignacio Santos
#
"""
Desarrollar un programa que pida un nombre y lo devuelva invertido, es decir que la primera letra pase a ser la última,
la segunda pase a ser la anteúltima, y así sucesivamente.
"""
#
# Obtenemos nombre
nombre = str(input('Ingrese un nombre: '))
nombreInv = ''
# Invertir nombre con bucle for
for i in range(len(nombre)-1, -1, -1):
    nombreInv = nombreInv + nombre[i]
# Imprimimos el resultado
print(f"El nombre invertido es: {nombreInv}")

"""
for i in range(0, len(nombre)-1, 1):
    nombreInv = nombre[i] + nombreInv
print(f"El nombre invertido es: {nombreInv}")
"""