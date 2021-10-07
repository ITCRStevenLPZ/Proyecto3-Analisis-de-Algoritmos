from math import ceil
import unittest

from dominio_ag_tsp import DominioAGTSP
from levenshtein import levenshtein

class PruebaDominioAGTSP(unittest.TestCase):

    __tsp = None

    @classmethod
    def setUpClass(cls):
        cls.__tsp = DominioAGTSP('datos/ciudades_cr_pruebas.csv', 'Alajuela')

    def test_generar_n(self):
        soluciones = self.__tsp.generar_n(10)
        self.assertEqual(len(soluciones), 10)
        for sol in soluciones:
            self.assertTrue(self.__tsp.validar(sol))

    def test_cruzar(self):
        sol_a, sol_b = self.__tsp.generar_n(2)
        hija = self.__tsp.cruzar(sol_a, sol_b)
        print(sol_a, sol_b, hija)
        self.assertTrue(self.__tsp.validar(hija))

    def test_mutar(self):
        sol = self.__tsp.generar()
        mutada = self.__tsp.mutar(sol)
        distancia = levenshtein(sol, mutada)
        # las soluciones no deben ser iguales
        self.assertGreater(distancia, 0)
        # las soluciones no deben variar en más del 50%
        self.assertLessEqual(distancia, ceil(len(sol) / 2))

    