# Fecha: 4/10/22
# Autor: Ignacio Santos
#
"""
Se está desarrollando una importante app para tratamiento de texto y nos piden que desarrollemos una función para una
de las opciones de la app. La función consiste en poner en mayúscula todas las vocales de una frase, por ejemplo, si la
función recibe el texto “frase de prueba para el nuevo programa de tratamiento de texto” debe devolver “frAsE dE prUEbA
pArA El nUEvO prOgrAmA dE trAtAmIEntO dE tExtO”.
Probar la función desde un programa principal con un input para la entrada de texto, luego la llamada a la función con
el texto como argumento, y finalmente un print de lo que la función devolvió.
"""
#
# Funcion consiste en poner mayúscula las vocales de una frase

# Variable que almacena el string
fraseConVocalesMayusc = ""
# Obtenemos la frase
frase = str(input("Ingrese la frase que va a transformar: "))
# Agregar todos los caracteres al otro string y si son vocales agregarlos en mayúsculas
for i in range(0, len(frase), 1):
    if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
        fraseConVocalesMayusc = fraseConVocalesMayusc + str.upper(frase[i])
    else:
        fraseConVocalesMayusc = fraseConVocalesMayusc + frase[i]
# Impresion de resultados
print(f"La frase transformada es: {fraseConVocalesMayusc}")


"""
# Variable para almacenar el string final
fraseConVocalesMayus = ""
# Obtener frase
frase = str(input("Ingresar la frase que desea transformar con vocales mayúsculas: "))
# Agregar todos los caracteres al otro string y si son vocales agregarlos en mayusculas
for i in range(0, len(frase), 1):
    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        fraseConVocalesMayus = fraseConVocalesMayus + str.upper(frase[i])
    else:
        fraseConVocalesMayus = fraseConVocalesMayus + frase[i]
# Imprimir resultados
print(f"La frase final es: {fraseConVocalesMayus}.")
"""


