# -*- coding: utf-8 -*-

''' 
Poblacion mundial

@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González
ÚLTIMA MODIFICACIÓN: Belén Ramos 11/10/2021

En este proyecto trabajaremos con datos de la evolución de la población mundial por países, 
representados mediante listas. Implementaremos una serie de funciones que nos permitirán analizar 
la evolución de la población y comparar la población de distintos países. 

CONJUNTOS DE DATOS:
-------------------
El proyecto incluye un conjuntos de datos de prueba:
  - population.csv: con los datos de población de diversos paises o agrupaciones de paises 
    en distintos años.
 
FUNCIONES QUE FORMAN PARTE DEL EJERCICIO:
-----------------------------------------
- lee_poblaciones(fichero):
    lee el fichero de entrada y devuelve una lista de tuplas 
    (nombre_pais, cod_pais, anyo, num_habitantes)
- calcula_paises(poblaciones):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y devuelve una lista ordenada con los nombres
    de los paises o conjuntos de paises para los que hay datos
- filtra_por_pais(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (anyo, num_habitantes)
    con los datos del pais que se pasa como parámetro. 
    El pais se puede dar con su nombre completo o con su código
- filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (nombre_pais, num_habitantes)
    con los datos del año pasado como parámetro para los paises 
    incluidos en el parámetro paises. 
'''

import csv
from collections import namedtuple

Poblacion = namedtuple('Poblacion', 'nombre, codigo, anyo, censo')

########################################################################################


def lee_poblaciones(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de tuplas poblaciones.
        Los tipos numéricos deben ser de tipo int.

    ENTRADA: 
        @param fichero: ruta del fichero csv que contiene los datos en codificación utf-8
        @type: fichero: str
    SALIDA: 
       @return lista de tuplas con la información de las poblaciones (nombre, código, anyo, censo)
       @rtype: [Poblacion(str,str,int,int)]
    '''
    pass
############################################################################################
############################################################################################


def calcula_paises(poblaciones):
    ''' A partir de la lista de poblaciones, calcula un lista ordenada con los nombres de los países para 
        los que hay al menos un dato de población. 
        La lista de salida no contendrá países repetidos.

    ENTRADA: 
       @param poblaciones: lista de tuplas Poblacion(nombre, código, anyo, censo) 
       @type: poblaciones: [Poblacion(str,str,int,int)]
    SALIDA: 
        @return: lista ordenada de nombres de los países
        @rtype: [str]
    '''
    pass
##############################################################################################
##############################################################################################


def filtra_por_pais(poblaciones, pais):
    '''A partir de la lista de poblaciones y del nombre o código de un país,  genera como salida
       una lista de tuplas con los datos de población del país dado por parámetro.  

    ENTRADA: 
        @param poblaciones: lista de tuplas Poblacion(nombre, código, año, censo) 
        @type: poblaciones: [Poblacion(str,str,int,int)]
        @param pais: nombre o código del país del que seleccionarán los registros
        @type: pais: str
    SALIDA: 
        @return lista de tuplas con la información de cada año y censo para el país dado (anyo, censo)
        @rtype: [(int,int)]
    '''
    pass
##############################################################################################

##############################################################################################


def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    ''' A partir de la lista de poblaciones, un año concreto y una lista de nombres de países,
    selecciona las tuplas correspondientes a un conjunto de paises de un año concreto

    ENTRADA: 
        @param poblaciones: lista de tuplas Poblacion(nombre, código, año, censo) 
        @type: poblaciones: [Poblacion(str,str,int,int)]
        @param anyo: año del que se buscan los datos de censo 
        @type: anyo: int
        @param paises: lista con los nombres de los países que se seleccionarán en los registros
        @type: pais: [str]
    SALIDA: 
        @return lista de tuplas con la el nombre de cada país y censo para el año dado (pais, censo)
        @rtype: [(str,int)]

    '''
    pass
##############################################################################################
