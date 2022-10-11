# Fecha: 4/10/22
# Autor: Ignacio Santos
#
"""
Se está desarrollando una mejora a un sitio web programado en Python al que se accede por una página que tiene seguridad
de ingreso por usuario y contraseña. Nos piden que desarrollemos una función que se va a usar para validar que las
contraseñas de los próximos cambios de password de los usuarios cumplan con las siguientes reglas:
• Deben tener como mínimo 8 caracteres de longitud
• Deben tener al menos 2 números
• Deben tener al menos 1 letra mayúscula
• Deben tener al menos 1 letra minúscula
La función deberá devolver True si la password pasa la validación, y en caso contrario False.
Probar la función desde un programa principal con un input para la entrada de la password, luego la llamada a la función
con la password como argumento, y finalmente un mensaje si pasó o no la validación.
"""

#
# Caracteristicas de la contraseña:
#           • Deben tener como mínimo 8 caracteres de longitud
#           • Deben tener al menos 2 números
#           • Deben tener al menos 1 letra mayúscula
#           • Deben tener al menos 1 letra minúscula

# Definimos la funcion que verificara la contraseña
# def verifContraseña(contraseña):
#    contraseña = contraseña
"""
def verificar_clave(passw):
    numeros = 0
    mayusculas = 0
    minusculas = 0

    if not 8 <= len(passw):
        return False

    for carac in passw:
        if carac.isnumeric():
            numeros += 1
        elif carac.isupper():
            mayusculas += 1
        elif carac.islower():
            minusculas += 1

    return numeros >= 2 and mayusculas != 0 and minusculas != 0


passw = input('Ingrese clave: ')

print(verificar_clave(passw))
"""


def validacion_Contra(contra):
    numeros = 0
    mayusculas = 0
    minusculas = 0

    if len(contra) <= 8:
        return False

    for i in range(0, len(contra), 1):
        if contra[i].isnumeric():
            numeros += 1
        if contra[i].isupper():
            mayusculas += 1
        if contra[i].islower():
            minusculas += 1

    if numeros >= 2 and mayusculas != 0 and minusculas != 0:
        return True
    else:
        return False


contra = input("Ingrese la contra: ")
print(validacion_Contra(contra))
