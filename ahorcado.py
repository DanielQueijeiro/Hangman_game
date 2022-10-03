import random

#bienvenida al juego
def bienvenida_juego():
    print("----------------------------------------------------------------")
    print("\n" "Bienvenido a Ahorcado, hecho por Daniel Queijeiro" "\n" )
    print("----------------------------------------------------------------")


bienvenida_juego()
#lista de palabras importada de un bloc de notas
with open("diccionario.txt", encoding="utf-8") as diccionario:
    palabras=diccionario.read()
palabra_aleatoria=palabras.split("\n")



#se selecciona una palabra aleatoria y se prepara para el juego
palabra_oculta = palabra_aleatoria[random.randint(0,29)]
palabra_oculta_tablero= list(palabra_oculta)
letras_correctas= " "
letras_incorrectas = " "
palabra=len(palabra_oculta)*"_"

#mostrar cuantas letras tiene su palabra
print("Su palabra contiene", "_" * len(palabra_oculta), len(palabra_oculta), " letras")

print("Al alcanzar 8 errores, pierdes")
#set errores a 0
e = 0

#adivinar y suma de errores (8 intentos)
while e < 8:
    intento = str((input("Escriba una letra para adivinar:  ")))
    print("----------------------------------------------------------------")
    if "a" <= intento <="z" and len(intento) ==1:#comprobar que el jugador intruduzca una letra valida
        if intento in palabra_oculta:
            letras_correctas = letras_correctas + intento
            for i in range(len(palabra_oculta)): #completar los espacios vacíos con las letras adivinadas
                if palabra_oculta[i] in letras_correctas:
                    palabra = palabra[:i] + palabra_oculta[i] + palabra[i+1:]
            print("Correcto, la palabra es:", palabra, "\n")
        elif intento not in palabra:#agregar letra erronea a lista
            e = e + 1
            letras_incorrectas = letras_incorrectas + intento + " "
            print(f"Incorrecto, tiene {e} error/es \nLa palabra es:", palabra, "\n ")
        print("Letras erroneas: ", letras_incorrectas)
        if palabra == palabra_oculta:#ganar
            print("Ganaste!, la palabra era:", palabra_oculta)
            quit()
    else:
            print("No es un carácter válido")
        
#perder
    if e == 8:
        print("Has alcanzado el maximo número de errores, perdiste \nLa palabra era:",palabra_oculta)