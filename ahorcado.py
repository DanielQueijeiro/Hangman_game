import random
#inicio del juego
print("Bienvenido a Ahorcado, hecho por Daniel Queijeiro")
#lista de palabras
lista = ["tarjeta", "pepinillo", "bocina", "codigo", "profesional"]
palabra = lista[random.randint(0,4)]
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
    i = str(input())
    if i in palabra:
        print("Correcto, la palabra es:")#como poner la palabra como "_,a,_,_,_,_,a"
        #ganar///como checar que la palabra ya este completa y proceder a ganar
        print("Correcto, la palabra es:", palabra[0:])
        quit()
    else:
        print(f"Incorrecto, tiene {e} error/es")
        e = e + 1
#perder
    if e == 7:
        print("Has alcanzado el maximo número de errores, perdiste")