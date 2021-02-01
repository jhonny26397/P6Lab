import unittest
from sudoku import Sudoku


class claseTest(unittest.TestCase):

    def setUp(self):
        self.instancia_uno  = Sudoku(1)
        self.instancia_dos  = Sudoku(2)
        self.instancia_tres = Sudoku(3)

        self.instancia_uno.cargarTablero()
        self.instancia_dos.cargarTablero()
        self.instancia_tres.cargarTablero()

    def tearDonw(self):
        pass

    """ TEST DE EL ORDEN DEL SUDOKU """
    """ La dimension del tablero """
    def testOrdenUno(self):
        self.assertEqual(1, self.instancia_uno.getTotalCasillas())

    def testOrdenDos(self):
        self.assertEqual(16, self.instancia_dos.getTotalCasillas())

    def testOrdenTres(self):
        self.assertLessEqual(81, self.instancia_tres.getTotalCasillas())


    """ TEST DEL CUADRADOS DE UN ELEMENTO """
    """ La dimension de un cuadro del tablero """
    def testCuadradoUno(self):
        self.assertLessEqual(1, self.instancia_uno.getCuadrado())

    def testCuadradoDos(self):
        self.assertLessEqual(4, self.instancia_dos.getTotalCasillas())

    def testCuadradoTres(self):
        self.assertLessEqual(9, self.instancia_tres.getTotalCasillas())


    """ TEST FILAS """
    def testFilaUno(self):
        result = self.instancia_uno.getFila(0)

        self.assertLessEqual([0], result)

    def testFilaDos(self):
        result = self.instancia_dos.getFila(1)

        self.assertLessEqual([0, 0], result)

    def testFilaTres(self):
        result = self.instancia_tres.getFila(2)

        self.assertLessEqual([0, 0, 0], result)

    """ TEST INDICES FINAL INICIAL """
    def testIndicesUno(self):
        inicio, final = 0, 0

        self.assertEqual(0, self.instancia_uno.getInicio(inicio))
        self.assertEqual(0, self.instancia_uno.getFinal(final))

    def testIndicesDos(self):
        inicio, final = 0, 1

        self.assertEqual(0, self.instancia_dos.getInicio(inicio))
        self.assertEqual(0, self.instancia_dos.getFinal(final))

    def testIndicesTres(self):
        inicio, final = 0, 2

        self.assertEqual(0, self.instancia_tres.getInicio(inicio))
        self.assertEqual(0, self.instancia_tres.getFinal(final))

if __name__ == "__main__":
    unittest.main()
