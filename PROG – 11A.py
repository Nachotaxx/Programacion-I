# Autor: Ignacio santos
# Fecha: 30/8/22
#
'''Escribir un programa que muestre la sumatoria de todos los
múltiplos de un número ingresado por el usuario, que se
encuentren entre el 0 y el 100.'''
#
n = int(input('Ingrese un numero que se encuentre entre[0,100]: '))
sumatoria = 0
#
for n in range(0, 100, n):
    print(n)
    sumatoria = sumatoria + n
    print()
print(f'La sumatoria es: {sumatoria}')
