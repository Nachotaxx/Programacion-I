# Autor: Ignacio Santos
# Fecha: 25/8/22
'''Tomando el ejercicio de estructuras selectivas cuyo enunciado
dice: “Una persona abona un producto, si el importe es menor
que el precio del producto, avisarle que el dinero es insuficiente. Si el
importe abonado es mayor, calcular el vuelto”, realizar
un nuevo algoritmo que ejecute la operación anterior de manera repetitiva y
 sólo termine cuando se ingresa un valor de
producto de cero pesos. Utilizar el ciclo apropiado.
'''
#
#
# Pedir al usuario que ingrese el precio del producto
precioProducto = input('Introduzca el precio del producto: ')
# Pedir al usuario que ingrese el importe
# Condicional para en parte mostrar que el dinero es insuficiente y en caso de
# que el importe sea mayor cálculo del vuelto
#
while int(precioProducto) > 0:
    importe = input('Con cuanto pagara?: ')  # Pedir al usuario que ingrese el importe
    if int(precioProducto) > int(importe) and int(precioProducto) > 0:
        print('El dinero es insuficiente')
    else:
        vuelto = int(importe) - int(precioProducto)
        print('Su vuelto es:', vuelto)


