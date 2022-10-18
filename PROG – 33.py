# Fecha 15/10/22
# Autor: Ignacio Santos
#
"""
Copiar todo el código del programa anterior.
Modificar la función listaDeItems para que ahora genere listas de números al azar entre 0 y 9, y además que las listas sean
de entre 1 y 20 elementos al azar. Probar el programa varias veces y observar que sucede cuando hay números comunes
repetidos, ya sea en la primera o segunda lista.
¿Qué se podría hacer para evitar que en la tercera fila que sale por pantalla no se muestren número repetidos? (Ayuda:
investigar en la documentación de Python el método de listas count() ver link)
"""

import random

"""
def listaDeItems():
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    lista = []
    largoLista = random.randint(5, 10)
    for x in range(0, largoLista):
        lista.append(random.choice(alfabeto))
    return lista


listaGenerada3 = []

listaGenerada1 = listaDeItems()
listaGenerada2 = listaDeItems()

for i in range (0,len(listaGenerada1), 1):
    if listaGenerada1[i] in listaGenerada2:
        listaGenerada3.append(listaGenerada1[i])
        
for i in range (0, len(listaGenerada3), 1):
    if listaGenerada3.count(i) > 1:
        #
    else:
        #

print(listaGenerada1)
print(listaGenerada2)
print(listaGenerada3)
"""


def listaDeItems():
    numeros = '0123456789'
    lista = []
    largoLista = random.randint(1, 20)
    for x in range(0, largoLista):
        lista.append(random.choice(numeros))
    return lista


listaGenerada3 = []

listaGenerada1 = listaDeItems()
listaGenerada2 = listaDeItems()

for i in range(0, len(listaGenerada1), 1):
    if listaGenerada1[i] in listaGenerada2:
        listaGenerada3.append(listaGenerada1[i])

"""
for i in range(0, len(listaGenerada1), 1):
    if listaGenerada1[i] in listaGenerada2:
        if listaGenerada1[i] == listaGenerada2:
            if listaGenerada1[i].count(listaGenerada2) == 0:
                listaGenerada3.append(listaGenerada1[i])
"""

"""
for i in range(0, len(listaGenerada3), 1):
    if listaGenerada3.count(i) > 1:
        listaGenerada3.remove(i)
    else:
        continue
"""
listaMayor = []
listaMenor = []

if len(listaGenerada1) > len(listaGenerada2):
    listaMayor = listaGenerada1
    listaMenor = listaGenerada2
else:
    listaMenor = listaGenerada1
    listaMayor = listaGenerada2

for i in range(0, len(listaMayor), 1):
    for j in range(0, len(listaMenor), 1):
        if listaMayor.count(listaMenor[j]) > 0:
            listaGenerada3.append(listaMenor[j])

lista4 = []

for i in range(0, len(listaGenerada3), 1):
    if lista4.count(listaGenerada3[i]) == 0:
        lista4.append(listaGenerada3[i])

# otra forma
for i in range(0, len(listaGenerada1), 1):
    elemento = listaGenerada1[i]
    for j in range(0, len(listaGenerada2), 1):
        elemento2 = listaGenerada2[j]
        if elemento == elemento2:
            if elemento.count(elemento2) == 0:
                listaGenerada3.append(elemento)

# conjunto3 = set()
conjunto3 = set(listaGenerada3)
# para ordenar el conjunto es:
listaGenerada3 = list(conjunto3)
listaGenerada3.sort()
# ordeno las listas generadas 1 y 2 para que sea mas claro
listaGenerada2.sort()
listaGenerada1.sort()

# otra forma de eliminar los elementos repetidos
listaGenerada3 = list(set(listaGenerada3))
listaGenerada3.sort()

# Imprimo TODAS las listas
print(listaGenerada1)
print(listaGenerada2)
# print(listaGenerada3)
print(listaGenerada3)  # ordenada

print(listaGenerada1)
print(listaGenerada2)
# print(listaGenerada3)

print(f"Lista menor: {listaMenor}")
print(f"Lista mayor: {listaMayor}")

lista4.sort()
print(f"Lista final: {lista4}")
