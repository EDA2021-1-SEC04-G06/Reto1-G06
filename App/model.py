"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import mergesort as sm
from DISClib.Algorithms.Sorting import quicksort as sq
assert cf
from DISClib.Algorithms.Sorting import listiterator as ite 

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categorias': None
               }

    catalog['videos'] = lt.newList(tipo)
    catalog['categorias'] = lt.newList(tipo)

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategorias(catalog, categoria):
    c = newCat(categoria['name'], categoria['id'])
    lt.addLast(catalog['categorias'], c)
   
# Funciones para creacion de datos

def newCat(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """

    cat = {'name': '', 'id': ''}
    cat['name'] = name
    cat['id'] = id
    return cat

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2): 
    """ 
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2 
    Args: 
        video1: informacion del primer video que incluye su valor 'views' 
        video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) < float(video2['views']))

# Funciones de ordenamiento

def requerimiento1(catalog, size,tipodeorden): 
    sublista = lt.subList(catalog['videos'], 0, size) 
    sublista = sublista.copy() 
    start_time = time.process_time() 
    if(tipodeorden=="shell"):
        sorted_list = sa.sort(sublista, cmpVideosByViews)
    elif (tipodeorden=="insertion"):
        sorted_list = si.sort(sublista, cmpVideosByViews)
    elif (tipodeorden=="selection"):
        sorted_list = ss.sort(sublista, cmpVideosByViews)
    elif (tipodeorden=="quick"):
        sorted_list = sq.sort(sublista, cmpVideosByViews)
    elif (tipodeorden=="merge"):
        sorted_list = sm.sort(sublista, cmpVideosByViews)
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return sorted_list

def requerimiento3(category_name, list, categories)->dict:
    for i in categories:
        if categories[i]== category_name:
            posicion= int(i)

    maximo=0
    extra=[]
    result={}
    iterador = ite.newIterator(list)
    contador= 0

    
    while ite.hasNext(iterador):
        element= it.next(iterador)
        centinela= True 
        contador1= 0


        if posicion == int(element["category_id"]):
            while contador1 < len(extra):
                if (element["title"])== extra[contador1]["title"]):
                    extra[contador1]["dias"] += 1
                    centinela= False
                contador += 1

        if centinela == True:
            extra.append({"title":element["title"],"channel_title":element["channel_title"],"category_id":element["category_id"], "dias":1, "dates":str(element["trending_date"])})


    while contador < len(extra):
        if int(extra[contador]["dias"]) > maximo:
            result["title"]= extra[contador]["title"]
            result["channel_title"]= extra[contador]["channel_title"]
            result["category_id"]= posicion
            result["dias"]=extra[contador]["dias"]
            maximo= int(extra[contador]["dias"])

        contador += 1
    return result 
