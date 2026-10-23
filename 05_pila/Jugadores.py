from cls_Stack import cls_Stack


class Jugadores:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partida = cls_Stack()
