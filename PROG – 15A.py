# Autor: Ignacio santos
# Fecha: 30/8/22
#
# Un colegio está organizando un viaje de egresados y necesita saber cuánto tendrá que pagar cada alumno y cuanto
# será el total a abonarle a la compañía de turismo.
# Si se inscriben 100 o más alumnos la empresa cobra 120.000 por alumno; si se inscriben entre 50 y 99 cobra 135.000 por
# alumno; si se inscriben de 30 a 49 cobra 150.000 por alumno; y si son menos de 30 un fijo total de 4.500.000
# Realizar un programa que solicite la cantidad de alumnos a inscribir, y muestre cuanto hay que cobrarle a cada
# uno por el pasaje, y cuanto hay que pagarle en total a la empresa.

# necesita saber cuanto pagara cada alumno y el total a abonar

cantAlumnos = int(input('Cuantos alumnos se inscribieron: '))

if cantAlumnos >= 100:
    print('La empresa cobrara 120000 por alumno')
    total = cantAlumnos * 120000
    print(f'El total a abonar es de {total}')
elif 50 <= cantAlumnos <= 99:
    print('La empresa cobrara 135000 por alumno')
    total = cantAlumnos * 135000
    print(f'El total a abonar es de {total}')
elif 30 <= cantAlumnos <= 49:
    print('La empresa cobrara 150000 por alumno')
    total = cantAlumnos * 150000
    print(f'El total a abonar es de {total}')
elif cantAlumnos < 30:
    print('La empresa cobrara 4500000')
    total = cantAlumnos * 4500000
    print(f'El total a abonar es de {total}')
