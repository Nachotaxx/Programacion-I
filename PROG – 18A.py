# Autor: Ignacio santos
# Fecha: 30/8/22
#
# Una empresa paga a sus empleados por semana trabajada. De cada empleado se conoce la cantidad de días trabajados en
# la semana y la cantidad de horas trabajadas en cada uno de esos días.
# Una particularidad de esta empresa es que el valor
# por hora a pagar es diferente para cada empleado. Informar lo que
# hay que pagarle por semana a cada empleado y cuál es el total general a pagar.
#
trabajadores = int(input('Ingrese la cantidad de trabajadores: '))
total = 0
for i in range(1, trabajadores+1, 1):
    dias = int(input(f'Ingrese la cantidad de dias trabajados del empleado {i}: '))
    valorHora = float(input('Ingrese el valor a pagar por hora del empleado: '))
    totalHoras = 0
    for j in range(1, dias+1, 1):
        horas = int(input(f'Ingrese las horas trabajadas para el dia {j}: '))
        totalHoras = totalHoras + horas

    sueldoSemanal = totalHoras * valorHora
    print(f'El sueldo del empleado {i} es:  ${sueldoSemanal}')
    total = total + sueldoSemanal

print(f'El total a pagar en la semana es: ${total:.2f}')

