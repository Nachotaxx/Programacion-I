# Autor: Ignacio santos
# Fecha: 30/8/22
#
'''Crear un programa que muestre los primeros N números de la
sucesión de Fibonacci. La sucesión comienza con los números
0 y 1 y, luego de éstos, cada nuevo elemento es la suma de los
dos números anteriores en la secuencia: Por ejemplo,
si N= 10, la sucesión es: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.'''
#
#
A = 0
B = 1
C = 0
n = int(input('Ingrese un numero: '))
print(A)
print(B)
for i in range(2, n, 1):
    C = int(A) + int(B)
    A = int(B)
    B = int(C)
    print(C)

