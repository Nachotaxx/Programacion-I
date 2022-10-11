# Autor: Ignacio santos
# Fecha: 30/8/22
#
# Mejorar el programa PROG-16A de manera tal que solo se puedan ingresar años desde el 2000
# en adelante y meses entre 1 y 12. Si se intentan ingresar otros valores, el programa debe volver a
# solicitar el dato avisando que lo que se ingresó es inválido y cuál es el rango válido de ingreso.
#

totalFacturado = float(input('Ingrese el total facturado: '))

while True:
    mes = int(input('Ingrese el mes que facturo: '))
    if 12 > mes > 1:
        break
    else:
        print('Mes invalido. Debe estar entre [1,12]')


while True:
    anio = int(input('Ingrese el anio que facturo: '))
    if anio >= 2000:
        break
    else:
        print('Anio invalido. Debe ser mayor a 2000')

cantidadDias = 0
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    cantidadDias = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    cantidadDias = 30
elif mes == 2:
    if ((anio % 4 == 0) and not (anio % 100 == 0)) or (anio % 400 == 0):
        cantidadDias = 29
    else:
        cantidadDias = 28


consumoDeGas = totalFacturado / cantidadDias

print(f'El valor diario facturado es de {consumoDeGas:.2f} ')
