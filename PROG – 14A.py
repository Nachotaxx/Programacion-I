# Autor: Ignacio santos
# Fecha: 30/8/22
#
# Desarrollar un programa que calcule la superficie de un círculo a partir del valor de su radio.

import math

radio = float(input('Introduzca el radio del circulo: '))

area = math.pi * radio**2

print(f'El area del circulo es: {area:.2f}')

