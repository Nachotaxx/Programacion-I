# Autor: Ignacio Santos
# Fecha: 13/09/22
#
# Ejercicio 1
# mientras = while

# Ejercicio 2
"""
A partir del ejercicio n°1, elaborar el programa en Python respetando las siguientes normas:
• Utilizar los siguientes identificadores: temperaturaDiaria ; temperaturaSemanal ;
promedioTemperatura ;
• El programa debe repetirse, una vez mostrado el promedio, se debe preguntar al
usuario si repetir el programa y el usuario debe responder SI o NO.
• No se deben aceptar temperaturas inferiores a - 20 y superiores a + 45
"""
"""
temperaturaSemanal = 0
temperaturaDiaria = 0
temperaturaPromedio = 0

print('Bienvenido!!!')

while True:

    for dia in range(1, 7 + 1, 1):
        temperaturaDiaria = float(input('Ingrese la temperatura de hoy: '))
        while temperaturaDiaria < -20 or temperaturaDiaria > 45:
            temperaturaDiaria = float(input('Ingrese valor valido: '))

        temperaturaSemanal = temperaturaSemanal + temperaturaDiaria

    temperaturaPromedio = temperaturaSemanal / 7

    print(f'La temperatura promedio es: {temperaturaPromedio:.2f} grados')

    seguir = input('Desea seguir otra semana [Si/No]: ')
    if seguir == 'no':
        break

print('Adios')
"""

# Ejercicio 4

"""
print("Bienvenido al calculador de alumnos")
acumuladorNota = 0
promedioNota = 0
contador = 0
notaAlumno = int(input("¿Cuál es la nota del " + str(contador + 1) + " ° alumno?: "))
while notaAlumno != 0:
    notaAlumno = int(input("¿Cuál es la nota del " + str(contador + 2) + " ° alumno?: "))
    contador = contador + 1
    acumuladorNota = acumuladorNota + notaAlumno
    promedioNota = acumuladorNota / contador

print("la nota de los " + str(contador) + " alumnos es de " + str(promedioNota) + " puntos")
"""

# Ejercicio 3

# Hacer un programa para hacer una Calculadora para dos números respetando las siguientes
# normas:
# • La calculadora debe solicitar al usuario ingrese dos números con los cuales operar.
# • Mensaje de bienvenida y pregunta al usuario entre las posibles operaciones a realizar,
# siendo estas: [S] suma, [R] resta, [M] multiplicación o [D] división,
# • Una vez que se imprima el resultado del cálculo, preguntar al usuario si desea realizar
# otra operación, para lo cual el usuario debe responder SI o NO. Si el usuario dice NO,
# mostrar mensaje de despedida y finalizar
# • La calculadora es solamente para dos números
# • Identificadores: numA ; numB ; suma ; resta ; multiplicación ; división
# • La calculadora NO debe permitir división sobre 0, en este caso, debe volver a pedir el
# segundo número


print('Bienvenido')
print()
numA = float(input('Ingrese el 1er numero: '))
numB = float(input('Ingrese el 2do numero: '))
continuar = 'si'
# numA != 0 and numB != 0
while True:
    suma = input('Desea sumar los numeros: [S] ')
    resta = input('Desea restar los numeros: [R] ')
    multipicacion = input('Desea multiplicar los numeros: [M] ')
    division = input('Desea dividir los numeros: [D] ')
    if suma == 'S':
        suma = numB + numA
        print(f'La suma es: {suma:.3f}')
    elif resta == 'R':
        resta = numA - numB
        print(f'La resta de los numeros es {resta:.3f}')
    elif multipicacion == 'M':
        multipicacion = numA * numB
        print(f'La multipicacion es {multipicacion:.3f}')
    elif division == 'D':
        while True:
            if numB == 0:
                print('Ingrese el numero devueta')
                numB = float(input('Ingrese el 2do numero: '))
            else:
                division = numA / numB
                print(f'La division es: {division:.3f}')
                break
    continuar = input('Desea continuar en la calculadora? ')
    numA = float(input('Ingrese el 1er numero: '))
    numB = float(input('Ingrese el 2do numero: '))
    if continuar == 'no':
        break
print('adios')


# Ejercicio 5

# En una Tienda de Sushi, para ayudar a los clientes a elegir del menú las piezas roll por su
# nombre de menú, se decidió hacer un programa que le vaya preguntando al cliente por cada
# uno de los ingredientes utilizados. El cliente decide si quiere o no incluir cada ingrediente.
# Finalmente, según los ingredientes elegidos, el programa le mostrará el nombre de menú del
# roll, así lo puede pedir por el nombre correcto.
# Las siguientes posibles son:
# SALMÓN + PALTA = NEW YORK ROLL
# SALMÓN + PEPINO = KAPPA ROLL
# SALMÓN + PEPINO + PALTA = MEX ROLL
# SALMÓN + PALTA + QUESO = PHILADELPHIA ROLL
# ATÚN + PEPINO + QUESO = TUNA ROLL
# SALMÓN + PEPINO + PALTA + QUESO = CALIFORNIA ROLL
# Tener en cuenta que, si alguna combinación de ingredientes no se corresponde con ningún
# roll del menú, el programa debe imprimir el mensaje de “pieza inexistente”.
# El programa debe contar con un mensaje al final para solicitarle al usuario si repetir la consulta
# o salir dando un mensaje de despedida.


print(f'''Que ingredientes desea agregar a su sushi,
    Entre ellos tenemos:
    1-Salmon
    2-Pepino
    3-Palta
    4-Queso
    5-Atun''')
"""
while True:
    ingredientes = str(input('Que ingredientes desea agregar? '))

    if ingredientes == 'salmon y palta':
        print('Le conviene el NEW YORK ROLL')
    elif ingredientes == 'salmon y pepino':
        print('Le conviene el KAPPA ROLL')
    elif ingredientes == 'salmon, palta y pepino':
        print('Le conviene el MEX ROLL')
    elif ingredientes == 'salmon, queso y palta':
        print('Le conviene el PHILADELPHIA ROLL')
    elif ingredientes == '':
        print()
"""
'''
while True:
    ingredientes = str(input('Que ingredientes desea agregar? '))

    if ingredientes == '1':
        if ingredientes == '2':
            print('NEW YORK ROLL')
'''
