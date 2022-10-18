# Fecha: 18/10/22
# Autor: Ignacio Santos

"""
Función que devuelve una lista de letras al azar tomadas del alfabeto.
DEPENDENCIAS:
Requiere importar el módulo random.
PARÁMETROS:
Ninguno.
SALIDA:
Lista de strings.
"""
import random


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


for i in range(0, len(listaGenerada1), 1):
    if listaGenerada1[i] in listaGenerada2:
        listaGenerada3.append(listaGenerada1[i])

for i in range(0, len(listaGenerada1), 1):
    for j in range(0, len(listaGenerada2), 1):
        if listaGenerada1[i] == listaGenerada2[j]:
            listaGenerada3.append(listaGenerada1[i])

for i in range(0, len(listaGenerada1), 1):
    elemento = listaGenerada1[i]
    for j in range(0, len(listaGenerada2), 1):
        elemento2 = listaGenerada2[j]
        if elemento == elemento2:
            listaGenerada3.append(elemento)


# otra forma
for i in range(0, len(listaGenerada1), 1):
    elemento = listaGenerada1[i]
    for j in range(0, len(listaGenerada2), 1):
        elemento2 = listaGenerada2[j]
        if elemento == elemento2:
            if listaGenerada3.count(elemento2) == 0:  # Si el elemento1 no esta en la lista
                listaGenerada3.append(elemento)

print(listaGenerada1)
print(listaGenerada2)
print(listaGenerada3)

