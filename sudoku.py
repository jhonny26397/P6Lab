import math


class Sudoku():
    def __init__(self, orden):
        self.__orden = orden

    def getTotalCasillas(self):
        return math.pow(self.__orden, 4)

    def getCuadrado(self):
        return math.pow(self.__orden, 2)

    def cargarTablero(self):
        elementos = self.__orden
        fila, tablero = [], []
        i = 0

        while i < elementos:
            fila = [(i * 0) for i in range(elementos)]
            tablero.append(fila)
            i += 1

        return tablero

    def getFila(self, fila):
        tablero = self.cargarTablero()
        elementos = self.__orden

        result = [tablero[fila][i] for i in range(elementos)]

        return result

    def getInicio(self, num):
        tablero = self.cargarTablero()
        return tablero[num][0]

    def getFinal(self, num):
        tablero = self.cargarTablero()
        return tablero[num][self.__orden - 1]
