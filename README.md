# Ahorcado
###### Contexto
El ahorcado es un juego de adivinanzas de lápiz y papel para dos o más jugadores. Un jugador piensa en una palabra, frase u oración y el otro trata de adivinarla según lo que sugiere por letras o dentro de un cierto número de oportunidades.
Usando una fila de guiones, se representa la palabra a adivinar, dando el número de letras. Si el jugador adivinador sugiere una letra o número que aparece en la palabra, el otro jugador la escribe en todas sus posiciones correctas. Si la letra o el número sugerido no ocurre en la palabra, el otro jugador saca un elemento de la figura de hombre palo ahorcado como una marca de conteo. El juego termina cuando:
- El jugador adivinador completa la palabra, o adivina la palabra completa correctamente
- El otro jugador completa el diagrama
###### Ejemplo
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Hangman.svg/100px-Hangman.svg.png)

El origen de este juego es incierto, pero a pesar de su pasado poco conocido, es uno de los juegos que probablemente todo el mundo conoce y esta familiarizado con el.
Es un juego sencillo de jugar y resulta entretenido.

El objetivo de este proyecto es recrear este juego a través de codigo Python3 de forma que el codigo le otorgue una palabra aleatoria al jugador y lleve la cuenta de los errores que el jugador vaya cometiendo.


# Algoritmos
(necesita mucha revisión)

Introducción

    print("Bienvenido a Ahorcado por Daniel Queijeiro")

¿escoger palabra aleatoria? (como se podría hacer para tener una colección de 5~ palabras para jugar)
Selección de la palabra aleatoria y presentarla al jugador

    var= palabra_random

    var2 = int(numero_de_letras_palabra) # letras que contiene la palabra

    print("La palabra es", var2 [numero_de_letras_palabra]) #(como representarlo como "_ _ _ _ _")#

El jugador empieza a adivinar letras y el programa le informa si acierta o no

    input(x) (jugador adivina una letra)

    if "input(x)" = letra_palabra = añadir letra a palabra

    print("Correcto, p _ _ _ _ ) #p solo es para ejemplar cuando se acierta la letra

	  else if "input(x)" = letra_no_palabra = añadir error a cuenta
  
      print("Error, x _ _ _ _ _ , quedan 5 intentos")
      
Se repite el proceso de adivinanza (como hacer para que el programa cheque si esta bien o mal)

      input(x) = letra_palabra = añadir letra a palabra (jugador adivina una letra) #sigue el juego

El programa detecta cuando la palabra este completa y termina el juego

    if letra_palabra = palabra completa

    print("Ganaste, la palabra era", var) #var=pizza solo es ejemplo de cuando se adivina toda la palabra

    Terminar

 El jugador ha alcanzado su limite de errores y pierde
 
	else if "input(x)" = letra_no_palabra = añadir error a cuenta
  
	if letra_no_palabra = 6° error
  
	print("Perdiste, la palabra era", var) #el jugador pierde
  
	Terminar
