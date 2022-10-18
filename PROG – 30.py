# Fecha: 11/10/22
# Autor: Ignacio Santos
#
"""
Escribir una función que reciba un número de mes y devuelva una cadena con el nombre del mes
Probar la función desde un programa principal con un input para la entrada del número de mes,
luego la llamada a la función con el número como argumento,
y finalmente un print de lo que la función devolvió.
"""


#
# funcion que seleccione a partir de un número el mes(string) en una lista
def numeroMesConv(mes):
    if 12 >= mes > 0:  # lo mismo que mes <= 12 and mes > 0:
        mesN = meses[mes - 1]  # variable que almacene la lista con sub índice
        # de la variable mes y -1 por la posición
        return mesN
    else:
        print("Ingrese numero valido")


# lista de meses
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
         "Octubre", "Noviembre", "Diciembre"]

# Obtenemos numero del mes
numeroMes = int(input("Ingrese el numero del mes: "))
nombreMes = numeroMesConv(numeroMes)

# imprimir los resultados
print(f"El numero del mes es {numeroMes}, y el mes es {nombreMes}")
