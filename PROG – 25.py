# Fecha: 4/10/22
# Autor: Ignacio Santos
#
"""
Una palabra es "alfabética" si todas sus letras están ordenadas alfabéticamente. Por ejemplo, "amor", "chino" e "himno"
son palabras "alfabéticas". Diseñar un programa que lea una palabra y nos diga si es alfabética o no.
"""


# creamos una funcion para validar si la palabra es alfa o no
def validacion(palabra):
    alfabetica = True
    for i in range(0, len(palabra) - 1, 1):
        if i - 1 > 0:
            if palabra[i - 1] > palabra[i - 2]:
                alfabetica = True
            else:
                alfabetica = False
                break
    return alfabetica


# Obtención de datos
palabra = str(input("Ingrese la palabra: "))
# Validar si es alfabetica
validacionPalabra = validacion(palabra)
# Mostramos datos
if validacionPalabra:
    print('La palabra es alfabetica')
elif not validacionPalabra:
    print('La palabra no es alfabetica')
