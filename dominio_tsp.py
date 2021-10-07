from dominio import Dominio
from datos import crear_datos
import random as rd
import collections


class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solución al problema.

    fcosto(sol)
        Calcula el costo asociado con una solución dada.

    vecino(sol)
        Calcula una solución vecina a partir de una solución dada.

    validar(sol)
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """

        self.ciudades, self.i_ciudades = crear_datos(ciudades_rutacsv)
        self.n_ciudades = len(self.ciudades)
        self.nombre_ciudad_inicio = ciudad_inicio
        self.i_ciudad_inicio = self.i_ciudades[ciudad_inicio]

    def validar(self, sol):
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """

        repetidos = [x for x, y in collections.Counter(sol).items() if y > 1]

        if len(sol) != self.n_ciudades-1:
            return False
        if repetidos != []:
            return False
        for entero in sol:
            if entero > len(sol):
                return False
            if self.i_ciudad_inicio == entero:
                return False
        return True

    def texto(self, sol):
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        formato_legible = self.nombre_ciudad_inicio + " -> "
        for ciudad in sol:
            nombre_actual = self.ciudades[ciudad]['km/min']
            formato_legible += nombre_actual + " -> "
        formato_legible += self.nombre_ciudad_inicio
        return formato_legible

    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """

        sol =  list(range(0,self.n_ciudades))
        del sol[self.i_ciudad_inicio]
        rd.shuffle(sol)        
        return sol

    def fcosto(self, sol):
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (list)
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """

        primera_visitada = self.ciudades[sol[0]]["km/min"]
        costo_ruta = float(self.ciudades[self.i_ciudad_inicio][primera_visitada])

        for i_ciudad in range(self.n_ciudades-2):
            ciudad_sig = self.ciudades[sol[i_ciudad+1]]['km/min']
            costo_ruta += float(self.ciudades[sol[i_ciudad]][ciudad_sig])
        
        ultima_ciudad = self.i_ciudades[ciudad_sig]
        costo_ruta += float(self.ciudades[ultima_ciudad][self.nombre_ciudad_inicio])

        return costo_ruta

    def vecino(self, sol):
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (list)
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (list) Solución vecina
        """
        temp = sol.copy()
        cambio_invalido = True
        cambios = 3
        while cambio_invalido or cambios == 0:
            i,j = rd.randint(0,self.n_ciudades-2),rd.randint(0,self.n_ciudades-2)
            temp[i],temp[j] = temp[j],temp[i]
            cambio_invalido = True
            if temp != sol:
                cambio_invalido = False
            cambios -=1
        return temp