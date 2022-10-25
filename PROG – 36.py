# Fecha: 25/10/22
# Autor: Ignacio Santos
#

import random


def leerArchivoTXT(rutaArchivo):
    archivo = open(rutaArchivo, encoding='utf8', mode='r')
    listaDeLineas = []
    linea = archivo.readline().replace('\n', '')
    while linea != "":
        listaDeLineas.append(linea)
        linea = archivo.readline().replace('\n', '')
    archivo.close()
    return listaDeLineas


listaTarjeta = leerArchivoTXT("/Users/ignaciosantos/Desktop/ub/tarjeta.txt")

print("""

SELECCIONE LA OPCIÓN DEL MENÚ

1 - Imprimir tarjeta

2 - Probar ingreso de clave

0 - Salir del sistema""")
print("\n")
opcion = int(input("opcion?: "))
print("\n")
if opcion == "0":
    print("Adios")
    exit()
if opcion == "1":
    for i in range(0, len(listaTarjeta), 1):
        print(listaTarjeta[i])
if opcion == "2":
    filaRandom = random.randint(1, 6)
    columnaRandom = random.randint(1, 9)
    valorClave = input(f"Ingrese el valor de la fila {filaRandom} y columna {columnaRandom}: ")
    if valorClave == listaTarjeta[filaRandom - 1][columnaRandom - 1]:
        print("PRUEBA DE INGRESO CORRECTA")
    else:
        print("INCORRECTO, VOLVER A PROBAR")

"""
# Importar librerias
import random

# Funciones
def cargarMatrizDesdeArchivo(rutaArchivo):
    archivo = open(rutaArchivo, encoding='utf8', mode='r')
    listaDeLineas = []
    linea = archivo.readline().replace('\n','').split(',')
    while linea != [""]:
        listaDeLineas.append(linea)
        linea = archivo.readline().replace('\n','').split(',')
    archivo.close()
    return listaDeLineas

# Mensaje inicio
opcionMenu = int(input("SELECCIONE LA OPCIÓN DEL MENU\n"
                       "1 - Imprimir tarjeta\n"
                       "2 - Probar ingreso de clave\n"
                       "0 - Salir del sistema\n"))
# Opción 0
if opcionMenu == 0:
    exit()
# Opción 1
matrizTarjeta = cargarMatrizDesdeArchivo("/Users/ignaciosantos/Desktop/ub/tarjeta.txt")
if opcionMenu == 1:
    print(matrizTarjeta)
# Opción 2
if opcionMenu == 2:
    # Generar valores random
    filaRandom = random.randint(1, 6)
    columnaRandom = random.randint(1, 9)
    # Ingresar un número
    numeroIngresado = input(f"Por favor ingresar el número ubicado en la fila {filaRandom} y en la columna {columnaRandom}: ")
    # Si el número ingresado es igual al valor que se encuentra en la matriz en esa posición devolver q es correcto
    if numeroIngresado == matrizTarjeta[filaRandom - 1][columnaRandom - 1]: # Se pone el valor - 1 porque la matriz empieza en 0
        print("El ingreso es correcto")
    else:
        print("Ingreso invalido")
        
"""
