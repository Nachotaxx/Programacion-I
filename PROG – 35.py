# Fecha: 18/10/22
# Autor: Ignacio Santos
#
"""
Una empresa que organiza maratones necesita un programa que genere un listado de los corredores indicando si llegaron
o no a la meta. El programa recibirá 2 archivos con nombres de corredores y emitirá un listado por pantalla.
Cuando comience la maratón, desde el punto de inicio del circuito enviarán un archivo conteniendo la lista de todos los
corredores que se registraron para la largada, ordenada por número de corredor. Cuando la maratón termine, desde el
final del circuito enviarán un archivo con la lista de los corredores que llegaron a la meta, ordenada según como fueron
llegando.

El programa debe leer ambos archivos y emitir un listado ordenado por número de corredor donde, a la derecha del nombre
se agregue la frase" – Tiempo empleado a determinar" para aquellos que arribaron a la meta, y para los que no llegaron se
agregue la frase " - Abandonó".
"""
"""
Función que lee un archivo de texto plano y devuelve su contenido como lista de líneas.
PARÁMETROS:
    rutaArchivo: Nombre del archivo a leer, incluyendo la ruta completa al archivo.
SALIDA:
    Lista de elementos strings conteniendo cada línea del archivo.
    Los caracteres de terminación de línea se descartan. 
"""


def leerArchivoTXT(rutaArchivo):
    archivo = open(rutaArchivo, encoding='utf8', mode='r')
    listaDeLineas = []
    linea = archivo.readline().replace('\n', '')
    while linea != "":
        listaDeLineas.append(linea)
        linea = archivo.readline().replace('\n', '')
    archivo.close()
    return listaDeLineas


listaLLegada = leerArchivoTXT("/Users/ignaciosantos/Desktop/ub/llegaron.txt")
listaPartieron = leerArchivoTXT("/Users/ignaciosantos/Desktop/ub/partieron.txt")


for corredor in range(0, len(listaPartieron)):
    if listaPartieron[corredor] not in listaLLegada:
        listaPartieron[corredor] = listaPartieron[corredor] + "Abandono"
    else:
        listaPartieron[corredor] = listaPartieron[corredor] + "Tiempo empleado a determinar"

listaPartieron.sort()

print(listaPartieron)

for i in listaPartieron:
    print(i)


