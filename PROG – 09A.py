# Autor: Ignacio santos
# Fecha: 30/8/22
'''
Hacer un algoritmo que, en base al precio de lista de un producto, muestre cuanto le costará al cliente según todas las
opciones de pago disponibles (si es en cuotas además del precio final que muestre el valor de cada cuota):
En efectivo: 10% de descuento
Tarjeta 1 pago: precio de lista
Tarjeta 3 pagos: 5% de recargo
Tarjeta 6 pagos: 10% de recargo
Tarjeta 12 pagos: 15% de recargo
Una vez mostrados los valores, el algoritmo debe esperar un nuevo ingreso, y sólo debe finalizar si se ingresa un precio
de 0 pesos (en dicho caso debe terminar sin calcular nada).
Algoritmo Efectivo_tarjeta
# 	//
# 	//Fecha:9/8/22
# 	//
# 	Escribir 'Cual es el precio del producto?'
# 	Leer precioProducto
# 	//
# 	//
# 	Mientras precioProducto > 0 Hacer
# 		//
# 		Escribir 'El precio al contado es: ', precioProducto * 0.9
# 		//
# 		Escribir 'El precio en un pago es: ', precioProducto
# 		//
# 		Escribir 'El precio en 3 cuotas: ', precioProducto * 1.05 / 3
# 		//
# 		Escribir 'El precio en 6 cuotas: ', precioProducto * 1.10 / 6
# 		//
# 		Escribir 'El precio en 12 cuotas: ', precioProducto * 1.15 / 12
# 		//
# 		Escribir 'Cual es el precio del producto?'
# 		Leer precioProducto
# 		//
# 	Fin Mientras
# 	//
# FinAlgoritmo
'''
#
#
precioProducto = float(input('Ingrese el precio del producto: '))
#
while precioProducto > 0:
    print(f'El precio al contado es: ${(precioProducto * 0.9):.2f}')
    print(f'El precio en un pago es: ${(precioProducto):.2f} ')
    print(f'El precio en 3 cuotas es: ${(precioProducto * 1.05 / 3):.2f} ')
    print(f'El precio en 6 cuotas es: ${(precioProducto * 1.10 / 6):.2f} ')
    print(f'El precio en 12 cuotas es: ${(precioProducto * 1.15 / 12):.2f}')
    precioProducto = float(input('Ingrese el precio del producto: '))
#
#
