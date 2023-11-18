#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#Escribe Hola Mundo en la consola
print("Hola Mundo")

# Crea un juego por consola de piedra, papel o tijera que interactue con dos usuarios, y los dos puedan elegir cualquiera de las 3 opciones. En cada ronda, los jugadores deben entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente. Además, se debe advertir al jugador si introduce una opción no válida, y se debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida. Por último, el jugador ve su puntuación al final del juego y puede elegir si vuelve a jugar.
def Juego():
    import random
    print("Bienvenido a Piedra, papel o tijera")
    def Jugar():
        print("Elije una de las siguientes opciones: Piedra, Papel o Tijera")
        player = input()
        player = player.lower()
        if player == "piedra" or player == "papel" or player == "tijera":
            print("Tu eliges: " + player)
        else:
            print("Esa no es una opción válida")
            Jugar()
        computer = random.randint(1,3)
        if computer == 1:
            computer = "piedra"
        elif computer == 2:
            computer = "papel"
        else:
            computer = "tijera"
        print("La computadora eligió: " + computer)
        if player == computer:
            print("Empate")
            Jugar()
        elif player == "piedra" and computer == "papel":
            print("Perdiste")
            Jugar()
        elif player == "papel" and computer == "tijera":
            print("Perdiste")
            Jugar()
        elif player == "tijera" and computer == "piedra":
            print("Perdiste")
            Jugar()
        else:
            print("Ganaste")
            Jugar()
    Jugar()
    print("Quieres volver a jugar? (Si/No)")
    again = input()
    again = again.lower()
    if again == "si":
        Juego()
    else:
        print("Gracias por jugar")

Juego()pier