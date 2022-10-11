# Autor: Ignacio Santos
# Fecha: 23/8/22
# Una persona abona un producto, si el importe es menor que el precio del
# producto, avisarle que el dinero es insuficiente. Si
# el importe abonado es mayor, calcular el vuelto.
#
# Pedir al usuario que ingrese el precio del producto
precioProducto = input('Introduzca el precio del producto: ')
# Pedir al usuario que ingrese el importe
importe = input('Con cuanto pagara?: ')
# Condicional para en parte mostrar que el dinero es insuficiente y en caso de
# que el importe sea mayor cálculo del vuelto
#
if precioProducto > importe:
    print('El dinero es insuficiente')
else:
    vuelto = int(importe) - int(precioProducto)
    print('Su vuelto es:', vuelto)
#
