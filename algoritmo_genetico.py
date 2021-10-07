
import dominio_ag_tsp
from math import ceil
import random
from multiprocessing import Process, Manager
import threading

def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps,testeo=False):
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (DominioAG)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la población.
    
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    
    reps (int)
        Número de iteraciones a ejecutar.
    
    testeo (bool)
        Booleano que permite recolección de datos adicionales para instrumentación

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """

    poblacion = dominio.generar_n(tam_pobl)
    costo = dominio.fcosto(poblacion[0])
    #print(costo)
    por_costo = lambda sol: dominio.fcosto(sol)
    #poblacion.sort(key=por_costo)     


    if testeo:
        datos = {"Fitness(costo ruta)":[costo],"Iteraciones":[0]}
        iteracion = 1
    

    for iterador_genetico in range(0, reps):
        nueva_poblacion = seleccion_poblacion(dominio, poblacion, ceil(tam_pobl * porc_elite))



        del poblacion[:]

        for iterator in range(0, tam_pobl):
            indice_padre_1 = random.randint(0, len(nueva_poblacion)-1)
            indice_padre_2 = random.randint(0, len(nueva_poblacion)-1)
            valor_mutacion = random.uniform(0, 1)
            hijo = dominio.cruzar(nueva_poblacion[indice_padre_1], nueva_poblacion[indice_padre_2])
            if valor_mutacion < prob_mut:
                hijo = dominio.mutar(hijo)
                poblacion.append(hijo)
            else:
                poblacion.append(hijo)     
        if testeo:
            #ordena_poblacion(dominio,poblacion)#Implementacion de quicksort para ordenar de menor a mayor en costo
            costo = dominio.fcosto(min(poblacion,key=por_costo))   
            datos["Fitness(costo ruta)"].append(costo)
            datos["Iteraciones"].append(iteracion)
            iteracion +=1
            
    if testeo:
        return poblacion[0],datos

    #ordena_poblacion(dominio,poblacion)                
    return min(poblacion,key=por_costo)


def seleccion_poblacion(dominio, poblacion, tamaño_elite):
    nueva_poblacion = []
    for iterador in range(0, tamaño_elite):
        indice_posible_padre_1 = random.randint(0, len(poblacion)-1)
        indice_posible_padre_2 = random.randint(0, len(poblacion)-1)
        posible_padre_1 = dominio.fcosto(poblacion[indice_posible_padre_1])
        posible_padre_2 = dominio.fcosto(poblacion[indice_posible_padre_2])
        if (posible_padre_1 <= posible_padre_2):
            nueva_poblacion.append(poblacion[indice_posible_padre_1])
        else:
            nueva_poblacion.append(poblacion[indice_posible_padre_2])

    return nueva_poblacion

def Iterar(nueva_poblacion,dominio,poblacion,prob_mut):
    indice_padre_1 = random.randint(0, len(nueva_poblacion)-1)
    indice_padre_2 = random.randint(0, len(nueva_poblacion)-1)
    valor_mutacion = random.uniform(0, 1)
    hijo = dominio.cruzar(nueva_poblacion[indice_padre_1], nueva_poblacion[indice_padre_2])
    if valor_mutacion < prob_mut:
        hijo = dominio.mutar(hijo)
        poblacion.append(hijo)
    else:
        poblacion.append(hijo)

#dominio_pruebas = dominio_ag_tsp.DominioAGTSP("datos/ciudades_cr.csv","Liberia")
#poblacion, datos = optimizar_concurrente(dominio_pruebas,200,0.1,0.1,200, data = True, Hilo = True)
#print(datos)
#print(poblacion)
