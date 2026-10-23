"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación II
Period.......: 3-2026
Documents....: Exam_01 - 01_Stack
Goals........: Using stack class
Professor....: Jorge Ruiz (york)
Student......: Emily Angelica Ramirez Matarrita
================================================================================================="""
from cls_Stack import cls_Stack

import time

from Jugador import Jugador
from Subrutinas import repartir_naipes


#Cambios que agregue para el main
jugadores = [
    Jugador("Merlina"),
    Jugador("Pericles"),
    Jugador("Tio Lucas"),
    Jugador("Homero")
]
repartir_naipes(jugadores)

print(f"{'Merlina':<15}{'Pericles':<15}{'Tio Lucas':<15}{'Homero':<15}") 
ganador = None
while any(not jugador.partida.isempty() for jugador in jugadores):

    for jugador in jugadores:
        if jugador.partida.isempty():
            continue

        naipe = jugador.partida.pop()
        print(f"{naipe:<15}", end="")

        if naipe == "QC":
            ganador = jugador
            print(f"\n¡{jugador.nombre} encontró Reina de Corazones!")
            break

        time.sleep(2)

    print()

    if ganador is not None:
        break
if ganador is not None:
    print(f"\nGanador: {ganador.nombre}")
else:
    print("\nNo hay naipes y no hubo ganador")
