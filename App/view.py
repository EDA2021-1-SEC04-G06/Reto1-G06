﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1 : Consultar cuales son los n videos con mas views de determinado pais y categoria")
    print("3- Requerimiento 2 : Consultar video que mas dias ha sio trending para determinado pais")
    print("4- Requerimiento 3 : Consultar video que mas dias ha sio trending para determinada categoria")
    print("5- Requerimiento 4 : Consultar cuales son los n videos con mas likes en un pais con tag especifico")
    print("0- Salir")

catalog = None

def initCatalog(tipo):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tipo)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printResults1(ord_vid, sample): 
    size = lt.size(ord_vid) 
    if size >= float(sample): 
        print("Los  ", sample, " videos con mas views son:") 
        i=0 
        while i <= float(sample): 
            videoo = lt.getElement(ord_vid,i) 
            print('Fecha de popularidad: '+videoo['trending_date'] +' Titulo: ' + videoo['title'] + ' Nombre del canal: '+videoo['channel_title']+' Fecha de publicacion: '+videoo['publish_time']+' Views: '+videoo['views']+' Likes: '+videoo['likes']+' Dislikes: '+videoo['dislikes']) 
            i+=1

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo = input('Ingrese el tipo de representacion de las listas: ( ARRAY_LIST o LINKED_LIST ) \n')
        catalog = initCatalog(tipo)
        loadData(catalog)
        print("Cargando información de los archivos ....")
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        primero = lt.firstElement(catalog['videos'])
        print("Info primer libro cargado: ")
        print(" Titulo: "+ str(primero['title'])+"\n Nombre del canal: "+ str(primero['channel_title'])+"\n Fecha de popularidad: "+ str(primero['trending_date'])+"\n Pais: "+ str(primero['country'])+"\n Vistas: "+ str(primero['views']) + "\n Likes: "+ str(primero['likes'])+"\n Dislikes: "+ str(primero['dislikes'])+"\n")
        print("Categorias :")
        print("Nombre , id" )
        for i in range(0,lt.size(catalog['categorias'])):
            cate = lt.getElement(catalog['categorias'], i)
            print(str(cate['name'])+" , "+str(cate['id']))

        
            
    elif int(inputs[0]) == 2:
        size = input("Indique tamaño de la muestra: ")
        tipodeorden = input("Indique el tipo de ordenamiento iterativo que quiere aplicar: ( selection, insertion, shell, quick o merge ) \n")
        result = controller.requerimiento1(catalog, int(size) , tipodeorden)
        #printResults1(result[1], size)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        

    else:
        sys.exit(0)
sys.exit(0)
