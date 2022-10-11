# Autor: Ignacio Santos
# Fecha: 23/8/22
# Realice un diagrama de flujo y pseudocódigo que representen el algoritmo para determinar cuánto pagará finalmente una
# persona por un artículo equis, considerando que tiene un descuento de 20 y debe pagar 21 de IVA (debe mostrar el
# precio con descuento y el precio final)
#
# Ingreso de datos
precioProducto = input('Introduzca el precio del producto: ')
# Calculos
descuento = float(precioProducto) * 0.20
iva = float(precioProducto) * 0.21
total = float(precioProducto) + iva - descuento
# Resultados
print('el descuento es:', int(descuento), 'el total:', int(total), 'el iva es:', int(iva),
      )
print('#############FACTURA###############')
print('El descuento es: $', int(descuento)
      )
#
print('El iva es: $', int(iva)
      )
#
print('El total es: $', int(total)
      )
print('###########FIN#FACTURA###############'
      )
