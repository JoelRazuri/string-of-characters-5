"""
    Escribir funciones que dadas dos cadenas de caracteres:
        a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
        es una subcadena de 'subcadena'.
        b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
        debe devolver 'gnome'.

"""


def es_subcadena(cadena1, cadena2):
    # Reicibe dos cadenas, si la cadena 2 esta dentro de la cadena 1 devulve True sino False.

    condicion = False

    if cadena2 in cadena1:
        condicion = True

    return condicion

# print(es_subcadena("subcadena","cadena"))
# print(es_subcadena("subcadena","Cadena"))


def orden_alfabetico(cadena1, cadena2):
    # Recibe dos cadenas y devuelve la que sea anterior en orden alfabetico.

    i = 0

    while True:
        if cadena1[i] == cadena2[i]:
            i+=1
        elif cadena1[i]<cadena2[i]:
            return cadena1
        else:
            return cadena2

print(orden_alfabetico("gnome","kde"))
print(orden_alfabetico("kra","kde"))
print(orden_alfabetico("kda","kde"))
