import random

#bienvenida al juego
def bienvenida_juego():
    print("----------------------------------------------------------------")
    print("\n" "Bienvenido a Ahorcado, hecho por Daniel Queijeiro" "\n" )
    print("----------------------------------------------------------------")


bienvenida_juego()
#lista de palabras
lista = ["compra", "juego", "codigo", "python", "pescado"]
diccionario = lista[random.randint(0,4)]
diccionario2= list(diccionario)
letras_correctas=[]
letras_incorrectas=[]
tablero=len(diccionario)*"_"
palabra = list(tablero)

#mostrar cuantas letras tiene su palabra
print("Su palabra contiene", "_" * len(diccionario), len(diccionario), " letras")

print("Al alcanzar 6 errores, pierdes")

#set errores a 0
e = 0

#adivinar y suma de errores (6 intentos)
while e < 6:
    intento = str((input("Escriba una letra para adivinar:  ")))
    print("----------------------------------------------------------------")
    if "a" <= intento <="z" and len(intento) ==1:
        if intento in diccionario2:
            for index, value in enumerate(diccionario2):
                if value == intento:
                    palabra[index] = intento
                if value != intento:
                    palabra[index] = "_"
            letras_correctas.append(intento)
            print("Correcto, la palabra es:", palabra, "\n")
        elif intento not in palabra:
                letras_incorrectas.append(intento)
                print(f"Incorrecto, tiene {e} error/es \n")
                e = e + 1
        print("Letras erroneas: ", letras_incorrectas)
        if palabra == diccionario2:#ganar///como checar que la palabra ya este completa y proceder a ganar
            print("Correcto, la palabra es:", diccionario)
            quit()
    else:
            print("No es un carácter válido")
        
#perder
    if e == 6:
        print("Has alcanzado el maximo número de errores, perdiste")