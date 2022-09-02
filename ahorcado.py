import random
from time import sleep


#inicio del juego
print("Bienvenido a Ahorcado, hecho por Daniel Queijeiro")
sleep(1)

#lista de palabras
lista = ["tarjeta", "pepinillo", "bocina", "codigo", "profesional"]
palabra = lista[random.randint(0,4)]

#mostrar cuantas letras tiene su palabra
print("Su palabra contiene", len(palabra), "letras")
palabra2 = palabra
palabra2 = list(palabra2)
sleep(1)
print("Al alcanzar 6 errores, pierdes")
sleep(1)

#set errores a 1
e = 1

#adivinar y suma de errores (6 intentos)
l = len(palabra)
while e < 7:
    print("Escriba una letra para adivinar/ Si cree saber cual es la palabra, introduzcala")
    i = str((input()))
    if i in palabra:
        for index, value in enumerate(palabra2):
            if value != i:
                palabra2[index] = "_"
        print("Correcto, la palabra es:", palabra2)
    else:
        if i != palabra2:
            print(f"Incorrecto, tiene {e} error/es")
            e = e + 1
    
    if i == palabra:#ganar///como checar que la palabra ya este completa y proceder a ganar
        print("Correcto, la palabra es:", palabra)
        quit()
        
#perder
    if e == 7:
        print("Has alcanzado el maximo número de errores, perdiste")