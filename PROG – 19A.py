# Autor: Ignacio Santos
# Fecha: 13/9/22
#
"""
Desarrollar un programa que pida dos valores enteros, valor1 y valor2, y que devuelva la sucesión de
enteros desde valor1 inclusive hasta valor2 inclusive, y junto a cada valor (en el sistema de numeración decimal)
su equivalente en hexadecimal
y su equivalente en binario. Validar que valor2 sea siempre mayor o igual a valor1.
La presentación debe ser bien legible en
formato tabular correctamente en columnado,
"""

"""
# PROG-19A
# Version 1.0
# Programa para
# Autor: Tomás Agustín Matteozzi y Matias Marzorati

# Obtencion de datos
valor1 = int(input("Ingresar valor 1: "))
valor2 = int(input("Ingresar valor 2: "))
# Realizar calculos si el valor 1 es más chico que el valor 2
if valor1 < valor2:
    print("DECIMAL      HEXADECIMAL         BINARIO\n======================================")
    for valor1 in range(valor1, valor2 + 1,1):
        print(valor1,"          ", hex(valor1),"            ", bin(valor1))
else:
    print("¡El valor 2 debe ser mayor al valor 1!")
"""

valor1 = int(input('Introduzca un numero: '))
valor2 = int(input('Introduzca un numero: '))

if valor1 < valor2:
    print('DECIMAL          HEXADECIMAL         BINARIO\n==================================================')

    for valor1 in range(valor1, valor2 + 1, 1):
        print(valor1,"                 ", hex(valor1),"              ",bin(valor1))

else:
    print('El valor 2 debe ser mayor al valor 1')
