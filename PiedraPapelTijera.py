import random  # Importa el módulo "random" para generar elecciones aleatorias.

lista = ["piedra", "papel", "tijeras"]  # Lista de opciones válidas para el juego.

computadora = random.choice(lista)  # La computadora elige aleatoriamente una opción de la lista.

jugador = None  # Inicializa la variable "jugador" para almacenar la elección del usuario.

info_computadora = "Computadora", computadora  # Almacena la elección de la computadora en una tupla con una etiqueta descriptiva.

while True:  # Bucle principal del juego. Se ejecuta indefinidamente hasta que el usuario decida salir.
    jugador = input("¿Piedra, Papel o Tijeras?").lower().strip()  # Solicita al usuario que ingrese su elección y normaliza la entrada (minúsculas y sin espacios).
    info_jugador = "Jugador", jugador  # Almacena la elección del jugador en una tupla con una etiqueta descriptiva.

    if jugador == computadora:  # Compara si la elección del jugador es igual a la de la computadora.
        print(info_computadora)  # Muestra la elección de la computadora.
        print(info_jugador)  # Muestra la elección del jugador.
        print("Empate")  # Indica que el resultado es un empate.
    elif jugador == "piedra":  # Si el jugador elige "piedra", entra en esta condición.
        if computadora == "tijeras":  # Compara si la computadora eligió "tijeras".
            print(info_computadora)  # Muestra la elección de la computadora.
            print(info_jugador)  # Muestra la elección del jugador.
            print("Ganaste")  # Indica que el jugador ganó.
        else:  # Si la computadora no eligió "tijeras", entonces eligió "papel".
            print(info_computadora)  # Muestra la elección de la computadora.
            print(info_jugador)  # Muestra la elección del jugador.
            print("Perdiste")  # Indica que el jugador perdió.
    elif jugador == "papel":  # Si el jugador elige "papel", entra en esta condición.
        if computadora == "piedra":  # Compara si la computadora eligió "piedra".
            print(info_computadora)  # Muestra la elección de la computadora.
            print(info_jugador)  # Muestra la elección del jugador.
            print("Ganaste")  # Indica que el jugador ganó.
        else:  # Si la computadora no eligió "piedra", entonces eligió "tijeras".
            print(info_computadora)  # Muestra la elección de la computadora.
            print(info_jugador)  # Muestra la elección del jugador.
            print("Perdiste")  # Indica que el jugador perdió.
    elif jugador == "tijeras":  # Si el jugador elige "tijeras", entra en esta condición.
        if computadora == "papel":  # Compara si la computadora eligió "papel".
            print(info_computadora)  # Muestra la elección de la computadora.
            print(info_jugador)  # Muestra la elección del jugador.
            print("Ganaste")  # Indica que el jugador ganó.
        else:  # Si la computadora no eligió "papel", entonces eligió "piedra".
            print(info_computadora)  # Muestra la elección de la computadora.
            print(info_jugador)  # Muestra la elección del jugador.
            print("Perdiste")  # Indica que el jugador perdió.

    jugar_de_nuevo = input("Desea jugar de nuevo si/no").lower().strip()  # Pregunta al usuario si desea jugar de nuevo.

    if jugar_de_nuevo != "si":  # Si la respuesta no es "si", sale del bucle.
        break  # Termina el bucle y finaliza el juego.

print("Hasta la proxima....")  # Mensaje de despedida cuando el usuario decide no seguir jugando.
