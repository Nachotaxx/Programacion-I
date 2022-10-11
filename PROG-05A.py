# Autor: Ignacio Santos
# Fecha: 23/8/22
# Un banco necesita establecer los nuevos límites de crédito de
# sus tarjetas. Las de tipo 1 aumentarán un 25%; las de tipo 2
# aumentarán un 35%; las de tipo 3 aumentarán un 40%, y las
# de cualquier otro tipo aumentarán un 50%. Desarrollar un
# algoritmo para calcular el nuevo límite según el límite
# actual y tarjeta del cliente.
#
# '''
# Algoritmo ejercicio3EsctructuraSelectivaCondicionMultiple
# 	//
# 	//Fecha:8/8/22
# 	//
# 	//Progama pide que se establezcan los nuevos limites de las tarjetas de credito.
# 	//Las de tipo1 aumentan 25%, tipo2 aumnetan 35%, de tipo3 40%, y de otro tipo 50%
# 	//de aumento. Calcular ese limite
# 	//
# 	Escribir 'Escriba el tipo de su tarjeta de credito'
# 	Escribir 'Escriba tipo1 si esta es su tarjeta'
# 	Escribir 'Escriba tipo2 si esta es su tarjeta'
# 	Escribir 'Escriba tipo3 si esta es su tarjeta'
# 	//Que el cliente escriba su tipo de tarjeta en el ejecutor
# 	Leer tipoDeTarjeta
# 	//Que el cliente escriba su limute anterior
# 	Escribir 'Cual era el limite de su tarjeta?'
# 	Leer limiteAnterior
# 	//
# 	//Utilizar comando de condicion multiple para que muestre el nuevo limite segun la tarjeta
# 	//
# 	Segun tipoDeTarjeta Hacer
# 		'tipo1':
# 			Escribir 'Las tarjetas de tipo1 tendran un 25% de aumento'
# 			nuevoLimite1 <- limiteAnterior * 0.25
# 			Escribir 'El nuevo limite es de: ', nuevoLimite1 + limiteAnterior
# 		'tipo2':
# 			Escribir 'Las tarjetas de tipo2 tendran un 35% de aumento'
# 			nuevoLimite2 <- limiteAnterior * 0.35
# 			Escribir 'El nuevo limite es de: ', nuevoLimite2 + limiteAnterior
# 		'tipo3':
# 			Escribir 'Las tarjetas de tipo3 tendran un 40% de aumento'
# 			nuevoLimite3 <- limiteAnterior * 0.40
# 			Escribir 'El nuevo limite es de: ', nuevoLimite3 + limiteAnterior
# 		De Otro Modo:
# 			Escribir 'Las tarjetas de este tipo tendran un 50% de aumento'
# 			nuevoLimite4 <- limiteAnterior * 0.5
# 			Escribir 'El nuevo limite es de: ', nuevoLimite4 + limiteAnterior
# FinSegun
# '''
#
#
print('Escriba el tipo de su tarjeta de credito ')
print('Escriba 1 si esta es su tarjeta ')
print('Escriba 2 si esta es su tarjeta ')
print('Escriba 3 si esta es su tarjeta ')
print('Escriba otra para cualquier otro tipo de tarjeta ')
#
print()
tipoDeTarjeta = input('Su tarjeta es: ')
##
print()
limiteAnterior = input('Escriba su limite anterior: ')
print()
##
# Primer if para la tarjeta de tipo 1
if tipoDeTarjeta == '1':
    print('Las  tarjetas de este tipo(1) tendran un 25% de aumento')
    nuevoLimite1 = float(limiteAnterior) * 0.25
    print()
    print('El nuevo limite es: ', nuevoLimite1 + float(limiteAnterior))
# Fin 1er if
#
print()
# Segundo if para tarjeta de tipo 2
if tipoDeTarjeta == '2':
    print('Las  tarjetas de este tipo(2) tendran un 35% de aumento')
    nuevoLimite2 = float(limiteAnterior) * 0.35
    print()
    print('El nuevo limite es: ', nuevoLimite2 + float(limiteAnterior))
# Fin 2do if
#
print()
# Tercer if para tarjeta de tipo 3
if tipoDeTarjeta == '3':
    print('Las  tarjetas de este tipo(3) tendran un 40% de aumento')
    nuevoLimite3 = float(limiteAnterior) * 0.40
    print()
    print('El nuevo limite es: ', nuevoLimite3 + float(limiteAnterior))
# Fin 3er if
#
print()
# Cuarto if para tarjeta de tipo cualquiera
if tipoDeTarjeta == 'otra':
    print('Las  tarjetas de este tipo(otro) tendran un 50% de aumento')
    nuevoLimite4 = float(limiteAnterior) * 0.50
    print()
    print('El nuevo limite es: ', nuevoLimite4 + float(limiteAnterior))
# Fin 4to if
