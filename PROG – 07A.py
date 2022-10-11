# Autor: Ignacio Santos
# Fecha: 25/8/22
'''Realizar un algoritmo que pida uno por uno los precios de
los productos comprados por el cliente en un mercado, y que al
ingresar un precio igual a cero muestre el total de la compra y
 la cantidad de productos. El cliente siempre compra al menos
un producto. Utilizar el ciclo apropiado.'''
#
#
productos = 0
factura = 0
precioProducto = float(input('Ingrese el precio del producto: '))
while float(precioProducto) != 0:
    productos = productos + 1
    factura = factura + precioProducto
    precioProducto = float(input('Ingrese el precio del producto: '))
#
if precioProducto == 0:
    print('El total de productos son: ', productos)
    print('El total de la compra es:', factura)

