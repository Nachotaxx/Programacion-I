# Fecha: 29/09/22
# Autor: Ignacio Santos
#
"""
Desarrollar un programa que pida el nombre de un mes y muestre la abreviación del mismo mes en 3 letras, en mayúsculas,
y finalizando con un punto. Por ejemplo, para enero devolverá ENE.
"""


# definimos una Funcion
def mesDelAno(mes):
    mes = mes.upper()
    mes = mes[0:3] + '.'
    return mes


mes = input('Ingrese el mes: ')

print(mesDelAno(mes))

"""
# Obtener mes
mes = str(input("Ingrese el nombre del mes que desea abreviar: "))
# Acortar string
mesAbreviado = mes[0:3]
# Imprimir resultado
print(f"La abreviación del mes es {str.upper(mesAbreviado)}.")
"""

# print(f"{mes[0:3]} {mes.upper()}")

while True:
    palabra = input('Ingrese palabra: ')
    alfabeticas = 0

    x = len(palabra)

    for i in range(0, x - 1, 1):

        if palabra[i] < palabra[i + 1]:
            print('Alfabetica')
        else:
            alfabeticas = False
            print('la palabra no es alfabetica')
            break
    if palabra == 'no':
        print('adios')
        break
