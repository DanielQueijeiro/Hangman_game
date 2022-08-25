#inicio del juego
from operator import index


print("Bienvenido a Ahorcado, hecho por Daniel Queijeiro")
print("Seleccione un numero del 0 al 4 para escoger su palabra")
#lista de palabras
lista = ["tarjeta", "pepinillo", "bocina", "codigo", "profesional"]
palabra = lista[(int(input()))]
#mostrar cuantas letras tiene su palabra
print("Su palabra contiene", len(palabra), "letras")
#print(palabra)
#set errores a 0
e = 0
#adivinar y suma de errores (7 intentos)
while e < 7:
    print("Escriba una letra para adivinar")
    if str(input()) in palabra:
        print("Correcto")
    else:
        print(f"Incorrecto, tiene {e + 1} error/es")
        e = e + 1
print("Perdiste")


#ganar


#perder
if e == 6:
    print("Ha alcanzadado el maximo numero de errores")