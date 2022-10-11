# Autor: Ignacio santos
# Fecha: 30/8/22
#
# Una empresa de suministros de gas factura a sus clientes mensualmente. La empresa necesita informarle a cada cliente
# cuál fue el valor que abonó por día por el consumo de gas, que se calcula dividiendo el total mensual
# que se facturó por la cantidad de días de dicho mes.
# Desarrollar un programa que, a partir de los datos de año, mes y total facturado,
# calcule el valor diario. Utilizar el código de
# cálculo de cantidad de días según mes y año que se mostró en la clase
# (Archivo: 50 - DIAS POR MES Y AÑO.txt).

# informar valor q abono por dia por el consumo de gas (total mensual / lo q se facturo por la cantidad de dias
# de ese mes

totalFacturado = float(input('Ingrese el total facturado: '))

mes = int(input('Ingrese el mes del anio que facturo: '))

anio = int(input('Ingrese el anio que facturo: '))

cantidadDias = 0
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    cantidadDias = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    cantidadDias = 30
elif mes == 2:
    if ((anio % 4 == 0) and not(anio % 100 == 0)) or (anio % 400 == 0):
        cantidadDias = 29
    else:
        cantidadDias = 28

consumoDeGas = totalFacturado / cantidadDias

print(f'El valor diario facturado es de ${consumoDeGas:.2f} ')
