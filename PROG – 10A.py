# Autor: Ignacio santos
# Fecha: 30/8/22
#
'''Escribir un programa que solicite al usuario un número que represente
una cantidad de veces (n), y luego itere dicha
cantidad de veces. En cada iteración, solicitar al usuario que ingrese un
número. Al finalizar, mostrar la suma de todos los
números ingresados.'''
#
#
n = int(input('Ingrese la cantidad de veces que quiera que se repita: '))
acumuladorSuma = 0
print('')
for n in range(0, n, 1):
    x = int(input('Ingrese un numero: '))
    acumuladorSuma = acumuladorSuma + x
print('')
print(f'La suma de los numeros ingresados es: {acumuladorSuma}')
