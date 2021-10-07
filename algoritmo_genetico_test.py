import unittest

from algoritmo_genetico import optimizar
from algoritmo_genetico import optimizar_concurrente
from dominio_ag_tsp import DominioAGTSP

class PruebaAlgoritmoGenetico(unittest.TestCase):

    def test_optimizar(self):
        dominio = DominioAGTSP('datos/ciudades_cr_pruebas.csv', 'Alajuela')
        sol = optimizar(dominio, 100, 0.1, 0.5, 1000)
        self.assertTrue(dominio.validar(sol))

    def test_optimizar_concurrente(self):
        dominio = DominioAGTSP('datos/ciudades_cr_pruebas.csv', 'Alajuela')
        sol = optimizar_concurrente(dominio, 100, 0.1, 0.5, 1000)
        self.assertTrue(dominio.validar(sol))
        