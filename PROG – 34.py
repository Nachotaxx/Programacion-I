# Fecha 15/10/22
# Autor: Ignacio Santos
#
"""
Se tienen estos 4 listados con los códigos de los trenes que se utilizan en las distintas líneas ferroviarias:
Línea San Martín
• Formación 011
• Formación 012
• Formación 013
• Formación 014

Línea Urquiza
• Formación 017
• Formación 002
• Formación 015
• Formación 014
• Formación 001
• Formación 004
• Formación 005

Línea Mitre A
• Formación 018
• Formación 028
• Formación 058
• Formación 048
• Formación 089
• Formación 009
• Formación 005

Línea Mitre B
• Formación 018
• Formación 028
• Formación 058
• Formación 048
• Formación 089

Primero, desarrollar un programa que muestre por pantalla los trenes para cada línea (similar a listado anterior).
Luego, ampliar el programa para que recorra todas las listas y cree una nueva lista con los trenes que son utilizados
en más de una línea.
"""


# Funcion
def impresionLinea(linea):
    for i in range(0, len(linea), 1):
        print(f" •{linea[i]}")
    print()


# Listas de las líneas de trenes
lineaSanMartin = ["Formación 011", "Formación 012", "Formación 013", "Formación 014"]
lineaUrquiza = ["Formación 017", "Formación 002", "Formación 015", "Formación 014", "Formación 001", "Formación 004",
                "Formación 005"]
lineaMitreA = ["Formación 018", "Formación 028", "Formación 058", "Formación 048", "Formación 089", "Formación 009",
               "Formación 005"]
lineaMitreB = ["Formación 018", "Formación 028", "Formación 058", "Formación 048", "Formación 089"]

lineas = [lineaSanMartin, lineaUrquiza, lineaMitreB, lineaMitreA]

trenesEnVariasLineas = []


# Linea San Martin
print("Linea San Martin")
impresionLinea(lineaSanMartin)
# Linea Urquiza
print("Linea Urquiza")
impresionLinea(lineaUrquiza)
# Linea Mitre A
print("Linea Mitre A")
impresionLinea(lineaMitreA)
# Linea Mitre B
print("Linea Mitre B")
impresionLinea(lineaMitreB)

# Luego, ampliar el programa para que recorra todas las listas y cree una nueva lista con los trenes que son utilizados
# en más de una línea.

"""
for i in lineaSanMartin + lineaUrquiza + lineaMitreA + lineaMitreB:
    trenesEnVariasLineas.append(i)


for formacion in lineaSanMartin + lineaUrquiza + lineaMitreA + lineaMitreB:
    if formacion.count() == 0:
        trenesEnVariasLineas.append(lineaUrquiza)

print(trenesEnVariasLineas)
"""
"""
for trenesMasUtilizados in lineaSanMartin:
    for i in lineaUrquiza:
        for j in lineaMitreA:
            for k in lineaMitreB:
                if lineaSanMartin.count(trenesMasUtilizados) == 0:
                    trenesEnVariasLineas.append(lineaSanMartin)

print(trenesEnVariasLineas)


for trenesMasUtilizados in lineas:
    if lineas.count() == 0:
        trenesEnVariasLineas.append()

print(trenesEnVariasLineas)


for i in range(0, len(lineas), 1):
    if lineaSanMartin[i] in lineas:
        if lineas.count(lineaSanMartin) == 0:
            trenesEnVariasLineas.append(lineaSanMartin)

    elif lineaUrquiza[i] in lineas:
        trenesEnVariasLineas.append(lineaUrquiza)
    elif lineaMitreA[i] in lineas:
        trenesEnVariasLineas.append(lineaMitreA)
    elif lineaMitreB[i] in lineas:
        trenesEnVariasLineas.append(lineaMitreB)
"""

"""
for trenesRepetidos in lineas:
    # Linea San Martin
    if lineaSanMartin in lineaUrquiza:
        trenesEnVariasLineas.append(lineaSanMartin)
    elif lineaSanMartin in lineaMitreA:
        trenesEnVariasLineas.append(lineaSanMartin)
    elif lineaSanMartin in lineaMitreB:
        trenesEnVariasLineas.append(lineaSanMartin)
    # Linea Urquiza
    if lineaUrquiza in lineaSanMartin:
        trenesEnVariasLineas.append(lineaUrquiza)
    elif lineaUrquiza in lineaMitreA:
        trenesEnVariasLineas.append(lineaUrquiza)
    elif lineaUrquiza in lineaMitreB:
        trenesEnVariasLineas.append(lineaUrquiza)
"""

# Linea San Martin
for formacion in lineaSanMartin:
    if formacion in lineaUrquiza:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)
    if formacion in lineaMitreA:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)
    if formacion in lineaMitreB:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)

# Linea Urquiza
for formacion in lineaUrquiza:
    if formacion in lineaSanMartin:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)
    if formacion in lineaMitreB:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)
    if formacion in lineaMitreA:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)

# Linea Mitre A
for formacion in lineaMitreA:
    if formacion in lineaSanMartin:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)
    if formacion in lineaMitreB:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)
    if formacion in lineaUrquiza:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)

# Linea Mitre B
for formacion in lineaMitreB:
    if formacion in lineaSanMartin:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)
    if formacion in lineaUrquiza:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)
    if formacion in lineaMitreA:
        if formacion not in trenesEnVariasLineas:
            trenesEnVariasLineas.append(formacion)

# for i in range(0, len(trenesEnVariasLineas), 1):
#     if trenesEnVariasLineas.remove(trenesEnVariasLineas[i]) == 0:
#         trenesEnVariasLineas.append(trenesEnVariasLineas[i])

"""
def repetidos(formacion):
    for formacion in lineas:
        if formacion in lineas:
            if formacion not in trenesEnVariasLineas:
                trenesEnVariasLineas.append(formacion)

    return trenesEnVariasLineas

print(repetidos(trenesEnVariasLineas))
"""

print(trenesEnVariasLineas)
print("Trenes en varias lineas: ")
impresionLinea(trenesEnVariasLineas)


