#inicio del juego
from operator import index


print("Bienvenido a Ahorcado, hecho por Daniel Queijeiro")
print("Seleccione un numero del 0 al 4 para escoger su palabra")
#lista de palabras
lista = ["tarjeta", "pepinillo", "bocina", "codigo", "profesional"]
palabra = lista[(int(input()))]
#mostrar cuantas letras tiene su palabra
print("Su palabra contiene", len(palabra), "letras")
print("Al alcanzar 6 errores, pierdes")
#print(palabra)
#set errores a 0
e = 1
#adivinar y suma de errores (6 intentos)
l = len(palabra)
while e < 7:
    print("Escriba una letra para adivinar")
    if str(input()) in palabra:
        print("Correcto, la palabra es:", l )
    else:
        print(f"Incorrecto, tiene {e} error/es")
        e = e + 1
#perder
print("Has alcanzado el maximo número de errores, perdiste")


#ganar
