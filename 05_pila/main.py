"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación III
Period.......: 3-2026
Documents....: Exam_01 - 01_Stack
Goals........: Using stack class
Professor....: Jorge Ruiz (york)
Student......: Emily Angelica Ramirez Matarrita
================================================================================================="""
from cls_Stack import cls_Stack

expresion = input("La expresión matemática es: ")

print()
print("Stack implementation")
print("=================================")

# Create stack instance
pilita = cls_Stack()

#Cambios al codigo
if not pilita.isempty():
    print("Error: la pila debe estar vacia.")
else:
    correcta = True

    cierres = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for caracter in expresion:

        if caracter in "([{":
            if not pilita.isfull():
                pilita.push(caracter)
            else:
                correcta = False
                break

        elif caracter in ")]}":

            if pilita.isempty():
                correcta = False
                break

            apertura = pilita.peek()

            if apertura == cierres[caracter]:
                pilita.pop()
            else:
                correcta = False
                break

    if not pilita.isempty():
        correcta = False

    while not pilita.isempty():
        pilita.pop()

    if correcta:
        print("Esta bien escrita la RegEx")
    else:
        print("Esta mal escrita la RegEx")


