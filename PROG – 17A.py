# Autor: Ignacio santos
# Fecha: 30/8/22
#
# Un empleado de una tienda realiza N ventas durante el día, se requiere saber cuántas de ellas fueron mayores a $1000,
# cuántas fueron mayores a $500 pero menores o iguales a $1000, y cuántas fueron menores o iguales a $500. Además, se
# requiere saber el monto de lo vendido en cada categoría y el monto total.
#
numeroDeVentas = int(input('Ingrese el numero de ventas: '))

ventasA = 0
ventasB = 0
ventasC = 0
subtotalA = 0
subTotalB = 0
subtotalC = 0
total = 0
contador = 1

while contador <= numeroDeVentas:
    monto = float(input('ingrese monto: '))
    if monto > 1000:
        ventasA = ventasA + 1
        subtotalA = subtotalA + monto
    elif monto > 500:
        ventasB = ventasB + 1
        subTotalB = subTotalB + monto
    else:
        ventasC = ventasC + 1
        subtotalC = subtotalC + monto

    total = total + monto
    contador = contador + 1

print(f'''Las ventas mayores a $1000 fueron: {ventasA}unidad/s , ${subtotalA:.2f}
Las ventas mayores a $500 fueron: {ventasB}unidad/s , ${subTotalB:.2f}
Las ventas menores a $500 fueron: {ventasC}unidad/s , ${subtotalC:.2f}
El total de la ventas fue de: ${total:.2f} ''')


