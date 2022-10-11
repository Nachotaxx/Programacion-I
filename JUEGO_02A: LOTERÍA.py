# Fecha: 27/09/22
# Autor: Ignacio Santos
# Programa juego lotería
#
"""
Idear un programa para emular la extracción de bolillas del juego de lotería de cartones (bingo).
Los números aleatorios van del 1 al 90 inclusive.
El programa deberá ir presentando el valor de las bolillas del juego sin repetición. Se deberá presionar la tecla ENTER
para presentar cada bolilla.
AYUDA: Para memorizar los números que van saliendo ir guardándolos en concatenación en una variable llamada
memoriaDeTiradas. Para saber si un número puede ser cantando buscarlo primero en la variable. (utilizar algún
mecanismo de concatenación que permita encontrar correctamente los números que fueron saliendo, por ejemplo, si
algunas tiradas atrás salió un 11 y fue memorizado, que si luego sale un 1 no informe que ya salió)
Una vez terminado, probar el programa en situación real jugando con los cartones azules hasta que alguien cante
¡BINGO! (se lleva premio:)
NOTA: En cada tirada, además de mostrar el valor de la bolilla, mostrar la variable memoriaDeTiradas, para que en el
caso de que un jugador cante Bingo se pueda verificar que completó correctamente su cartón.
"""

# numeros aleatorios del 1 al 90 *
# valor de las bolitas sin repeticion
# TECLA ENTER para presentar cada bolita *
# Guardar numeros en variable memoriaDeTiradas, para mostrar otro numero
# primero debe revisar si ya estuvo en la variable
#
# En cada tirada mostrar el valor de la bolita, variable(memoriaDeTiradas)

# importamos modulo
import random

"""
memoria = ""
while True:
    # Sacar bolilla
    bolilla = str(random.randint(1, 90))

    # Presionar tecla para continuar
    input('Presionar tecla para continuar')

    # Memorizar bolillas
    # Al iniciar:

    # Cuando memoriza:

    print(memoria)
    if memoria.find(" " + str(bolilla) + " ") == -1:
        memoria = memoria + " " + str(bolilla) + " "

    print(f'''{bolilla}
    {memoria}''')
#
"""

# IMPORTACIÓN DE MÓDULOS
import random  # Necesario para generar los números aleatorios del bolillero

# DECLARACIÓN DE FUNCIONES
"""
Función para determinar si un valor de bolilla ya fue cantado en extracciones anteriores.
PARÁMETROS:
    bol: string con el valor de bolilla que se quiere revisar si salió previamente.
    mem: string conteniendo todos los valores de bolilla que salieron previamente.
SALIDA:
    True: si bol está dentro de mem, es decir si ya salió la bolilla.
    False: si bol no está dentro de mem, es decir si la bolilla aún no salió.
"""


def yaCantado(bol, mem):
    posicion = mem.find(" " + bol + " ")  # Busca bol dentro de mem, devuelve -1 si no lo encuentra
    if posicion == -1:  # Si no encuentra bol dentro de mem ...
        return False  # ... la bolilla no fue cantada
    else:  # Si encuentra bol dentro de mem ...
        return True  # ... la bolilla ya fue cantada


# PROGRAMA PRINCIPAL
memoria = ""  # Variable para almacenar los valores de bolilla que van saliendo.
print()
input("Presione ENTER para sacar la primera bolilla.")

while True:  # Este bucle se repite por cada extracción de bolilla
    while True:  # Este bucle se repite hasta que se obtiene una bolilla que no haya salido
        bolilla = str(random.randint(1, 90))  # Se genera un valor de bolilla de 1 a 90 y se lo covierte a string
        if yaCantado(bolilla, memoria) == False:  # Sólo sale del bucle si se obtiene un valor de bolilla que no
            # haya salido
            break
    print()
    print("¡CANTAR! >>>>> " + bolilla + " <<<<<")
    memoria = memoria + " " + bolilla + " "  # Se almacena el valor cantado. El patrón de almacenamiento es
    # espacio+valor+espacio
    print("Ya cantados: ", memoria)
    print()
    input("Presione ENTER para sacar otra bolilla.")
