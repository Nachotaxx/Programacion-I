# Fecha: 6/10/22
# Autor: Ignacio Santos
#
"""
Escribir una función que reciba una cadena que contiene un número entero de muchos dígitos y devuelva una cadena con
el mismo número pero con los puntos de las separaciones de miles. Por ejemplo, si recibe 1234567890, debe devolver
1.234.567.890
"""

# Nos pide funcion que reciba cadena de numeros y devuelva la misma con separaciones de puntos
#
#

num = int(input('Ingrese el numero entero: '))
cad = str(num)
cad2 = ""
cont = 1
for caracter in cad[::-1]:
    cad2 = caracter + cad2
    if cont % 3 == 0:
        cad2 = "." + cad2
    cont += 1
print(cad2)


def separacionPuntos(cad2):
    cadena = str(num)
    contador = 1
    for caracter in cad[::-1]:
        cad2 = caracter + cad2
        if contador % 3 == 0:
            cad2 = "." + cad2
        contador += 1
    return cad2


num = int(input('Ingrese cadena: '))
cad2 = ""
print(separacionPuntos(cad2))
