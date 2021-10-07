from dominio_ag import DominioAG
from dominio_tsp import DominioTSP
from random import random

class DominioAGTSP(DominioAG, DominioTSP):
    """
    Representa el objeto de dominio que conoce los detalles de implementación y modelamiento
    del problema del vendedor viajero para ser resuelto con algoritmos genéticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar(n)
        Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

    cruzar(sol_a, sol_b)
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol)
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero para ser resuelto
        con algoritmos genéticos.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioAGTSP correctamente inicializada.
        """
        
        super().__init__(ciudades_rutacsv,ciudad_inicio)

    def generar_n(self, n):
        """Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (sols) Lista que contiene n listas, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """
        
        sols = []
        for x in range(n):
            nuevo = self.generar()
            valido = self.validar(nuevo)
            while(not valido):
                nuevo = self.generar()
                valido = self.validar(nuevo)
            sols.append(nuevo)
        return sols

    def cruzar(self, sol_a, sol_b):
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (H1) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """

        P1 = sol_a
        P2 = sol_b
        lenOri = len(sol_a)
        H1 = [-1] * lenOri
        geneA = 0
        geneB = 0
        while (geneA == geneB):#para que lo rango no sea igual a vacio
            geneA = int(random() * lenOri)
            geneB = int(random() * lenOri)

        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)

        for i in range(startGene, endGene):
            H1[i] = P1[i]
        rec = 0#recorrido del padre
        recorrido = 0#pos en la que va el nuevo elemento
        while (rec < lenOri):
            while (H1[recorrido] != -1 and recorrido + 1 < lenOri):
                recorrido += 1
            if (P2[rec] not in H1):
                H1[recorrido] = P2[rec]
            rec += 1
        return H1


    def mutar(self, sol):
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (estructura de datos)
            La solución a mutar.
        
        Salidas:
        (vecino(sol)) Una nueva solución que refleja un ligero cambio con respecto 
        a la solución dada por parámetro utilizando el método de vecino del SIM ANNEALING
        """

        return super().vecino(sol)