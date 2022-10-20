import random
from time import sleep

# bienvenida al juego


def bienvenida_juego():
    print("----------------------------------------------------------------")
    print("""\n" "Bienvenido a Ahorcado, hecho por Daniel Queijeiro
  +---+
  |   |
      |
      |
      |
      |
=========""")
    print("----------------------------------------------------------------")
    sleep(1.5)


bienvenida_juego()

# Establecer palabras con dificultades a traves de una matriz
facil = ["compra", "juego", "patata", "python", "virus"]
intermedio = ["pescado", "conducta", "terapia", "troyano", "rebasar"]
dificil = ["procedimiento", "eternidad", "hospital", "circular", "espectador"]
palabra_aleatoria = [facil, intermedio, dificil]


# se selecciona una palabra aleatoria y se prepara para el juego
palabra_oculta = palabra_aleatoria[int(input(
    """Introduzca la dificultad que desee
0=Facil
1=Intermedio
2=Dificil
"""))][random.randint(0, 4)]
print("----------------------------------------------------------------")
palabra_oculta_tablero = list(palabra_oculta)
letras_correctas = " "
letras_incorrectas = " "
palabra = len(palabra_oculta) * "_"

# mostrar cuantas letras tiene su palabra
print("Su palabra contiene", "_" * len(palabra_oculta),
      len(palabra_oculta), " letras")
      
print("Al alcanzar 10 errores, pierdes")
# set errores a 0
e = 0

# adivinar y suma de errores (10 intentos)
while e < 10:
    intento = str((input("Escriba una letra para adivinar:  ")))
    print("----------------------------------------------------------------")
    # comprobar que el jugador intruduzca una letra valida
    if "a" <= intento <= "z" and len(intento) == 1:
        if intento in palabra_oculta:
            letras_correctas = letras_correctas + intento
            # completar los espacios vacíos con las letras adivinadas
            for i in range(len(palabra_oculta)):
                if palabra_oculta[i] in letras_correctas:
                    palabra = palabra[:i] + palabra_oculta[i] + palabra[i + 1:]
            print("Correcto, la palabra es:", palabra, "\n")
        elif intento not in palabra:  # agregar letra erronea a lista
            e = e + 1
            letras_incorrectas = letras_incorrectas + intento + " "
            print(
                f"Incorrecto, tiene {e} error/es \nLa palabra es:",
                palabra,
                "\n ")
        print("Letras erroneas: ", letras_incorrectas)
        if palabra == palabra_oculta:  # ganar
            print("Ganaste! a palabra era:", palabra_oculta)
            quit()
    else:
        print("No es un carácter válido")

# perder
    if e == 10:
        sleep(1)
        print("""\n----------------------------------------------------------------
Has alcanzado el maximo número de errores, perdiste.
La palabra era:""", palabra_oculta,
              """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========
----------------------------------------------------------------""")
