# Autor: Ignacio santos
# Fecha: 30/8/22
#
"""Dado un número entero positivo, mostrar su factorial.
El factorial de un número se obtiene multiplicando todos los números
enteros positivos que hay entre el 1 y ese número.
Por ejemplo, el factorial de 5, es 120. (5! = 120)"""
#

from math import factorial
n = int(input('ingrese un numero: '))
print('El factorial es: ', factorial(n))
#
#
numero = int(input('Ingrese un numero: '))
factorial = 1
if numero != 0:
    for i in range(1, numero+1):
        factorial = factorial*i
print('El factorial es', factorial)
#
#
numero = int(input('Ingrese un numero: '))
factorial = 1

for i in range(1, numero+1):
    factorial = factorial * i
if numero == 0:
    print('No es posible')
print('El factorial es ', factorial)
