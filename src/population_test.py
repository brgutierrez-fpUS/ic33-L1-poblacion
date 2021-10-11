# -*- coding: utf-8 -*-
'''
Created on 12 oct. 2018

@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González
ÚLTIMA MODIFICACIÓN: Belén Ramos 11/10/2021

Archivo con pruebas para el proyecto de poblaciones
'''

from population import *

################################################################
#  Funciones auxiliares
################################################################


def mostrar_numerado(coleccion):
    i = 0
    for p in coleccion:
        i = i+1
        print(i, p)

################################################################
#  Funciones de test
################################################################


def test_lee_poblaciones():
    print("Leidos ", len(POBLACIONES), "datos de población mundial")
    mostrar_numerado(POBLACIONES)


def test_calcula_paises():         # Test de la función calcula_paises
    pass


def test_filtra_por_pais():         # Test de la función filtra_por_pais
    pass


def test_filtra_por_paises_y_anyo():         # Test de la función filtra_por_paises_y_anyo
    pass


################################################################
#  Programa principal
################################################################
POBLACIONES = lee_poblaciones('../data/population.csv')

# test_lee_poblaciones()
# test_calcula_paises()
# test_filtra_por_pais()
# test_filtra_por_paises_y_anyo()
