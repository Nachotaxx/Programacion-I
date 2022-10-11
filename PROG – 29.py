# Fecha: 11/10/22
# Autor: Ignacio Santos
#
"""
Escribir un programa donde se declare la misma lista de temperaturas del ejercicio anterior y realice lo siguiente:
        • Ordenar las temperaturas de menor a mayor
        • Obtener la temperatura mínima y la máxima del mes
        • Obtener la temperatura promedio del mes
        • Calcular la cantidad de días con temperatura bajo cero
Y luego muestre la información de esta forma:
TEMPERATURAS DE JULIO (de menor a mayor)
========================================
temp
temp
temp
...
TEMPERATURAS
=====================
MIN: temp
MAX: temp
PROMEDIO: temp
CANTIDAD DE DÍAS BAJO CERO: n
"""
#

Temperaturas = [15, 13.5, 5.1, 3, 2.2, -2, -5, 8, 10, 7.3, 6, 3.3, 0, -1, 10, 8.5,
                0, 2, -4, -3.7, 0, 4.6, 5, 3, -0.5, 1, 0, -1, 4, 2.9, -3.1]

print("""
TEMPERATURAS DE JULIO (de menor a mayor)
========================================""")
Temperaturas.sort()
print(Temperaturas)

for Temperatura in Temperaturas:
    print(Temperatura)

print("""
TEMPERATURAS
=====================""")

print("MIN:", Temperaturas[0])
print("MAX:", Temperaturas[-1])

contadorBajoCero = 0
totalTemperaturas = 0
for i in range(0, len(Temperaturas), 1):
    totalTemperaturas = totalTemperaturas + Temperaturas[i]
    if Temperaturas[i] < 0:
        contadorBajoCero += 1

promedio = totalTemperaturas / len(Temperaturas)
print("PROMEDIO:", promedio)

print(f"CANTIDAD DE DÍAS BAJO CERO: {contadorBajoCero}")

