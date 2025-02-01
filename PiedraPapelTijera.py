import random

lista = ["piedra","papel","tijeras"]
computadora = random.choice(lista)
jugador = None

info_computadora = "Computadora",computadora

while True:
    jugador = input("¿Piedra, Papel o Tijeras?").lower().strip()
    info_jugador = "Jugador", jugador
    if jugador == computadora:
        print(info_computadora)
        print(info_jugador)
        print("Empate")
    elif jugador == "piedra":
        if computadora == "tijeras":
            print(info_computadora)
            print(info_jugador)
            print("Ganaste")
        else:
            print(info_computadora)
            print(info_jugador)
            print("Perdiste")
    elif jugador == "papel":
        if computadora == "piedra":
            print(info_computadora)
            print(info_jugador)
            print("Ganaste")
        else:
            print(info_computadora)
            print(info_jugador)
            print("Perdiste")
    elif jugador == "tijeras":
        if computadora == "papel":
            print(info_computadora)
            print(info_jugador)
            print("Ganaste")
        else:
            print(info_computadora)
            print(info_jugador)
            print("Perdiste")
    jugar_de_nuevo = input("Desea jugar de nuevo si/no").lower().strip()

    if jugar_de_nuevo != "si":
        break

print("Hasta la proxima....")
