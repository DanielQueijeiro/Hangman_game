from dataclasses import replace
import random
from time import sleep






#bienvenida al juego
def bienvenida_juego():
    print("Bienvenido a Ahorcado, hecho por Daniel Queijeiro")
    sleep(1)


bienvenida_juego()
#lista de palabras
lista = ["tarjeta", "pepinillo", "bocina", "codigo", "profesional"]
diccionario = lista[random.randint(0,4)]
diccionario = list(diccionario)
print(diccionario)
tablero=len(diccionario)*"_"

#mostrar cuantas letras tiene su palabra
print("Su palabra contiene", "_" * len(diccionario), len(diccionario), "letras")
sleep(1)
print("Al alcanzar 6 errores, pierdes")
sleep(1)

#set errores a 1
e = 1

#adivinar y suma de errores (6 intentos)
while e < 7:
    print("Escriba una letra para adivinar/ Si cree saber cual es la palabra, introduzcala")
    i = str((input()))
    if diccionario == tablero:
        print("ganaste")
    elif "a" <= i <="z" and len(i) ==1:
        if i in diccionario:
            for index, letra_palabra in enumerate(diccionario):
                if i == letra_palabra:
                    tablero[index] = i
            print("Correcto, la palabra es:", tablero)
        elif i not in diccionario:
                print(f"Incorrecto, tiene {e} error/es")
                e = e + 1
        
        if i == diccionario:#ganar///como checar que la palabra ya este completa y proceder a ganar
            print("Correcto, la palabra es:", diccionario)
            quit()
    else:
        print("No es un carácter válido")
        
#perder
    if e == 7:
        print("Has alcanzado el maximo número de errores, perdiste")