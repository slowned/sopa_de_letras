from random import randint
from utilidades import *

"""
    - Funciones para generar ubicacion aleatorio de las palabras
    - Recibimos una Lista con las palabras listas para cargar en la Grilla
"""

#IMPORTANTE: REEMPLAZAR len(palabras) por: palabra.longitud
def dimensionGrillaHorizontal(lista_palabras):
    """
            ->Recibe una Lista de Objeto palabras
            ->Retorna la dimension de grilla para ubicar palabras HORIZONTALMENTE
    """
    dim_columna = 0
    dim_fila = len(lista_palabras)
    for palabra in lista_palabras:
        if(len(palabra) > dim_columna):
            dim_columna = len(palabra)
    return(dim_fila, dim_columna)

def dimensionGrillaVertical(lista_palabras):
    """
                ->Recibe una Lista de Objeto palabras
                ->Retorna la dimension de grilla para ubicar palabras VERTICALMENTE
    """
    columna, fila =dimensionGrillaHorizontal(lista_palabras)
    return(fila, columna)


def generarPosicionHorizontal(palabra,dim_fila, dim_columna):
    """
        Funcion que genera la posicion de una palabra, para una grilla de Distribucion HORIZONTAL
        -> Recibe un Objeto Palabra
        -> Agrega un posicion al objetoPalabra: objeto.posicion(posicion)
    """
    len_palara = palabra.longitud
    columna = randint(0, (dim_columna -len_palabra))
    fila = randint(0,dim_fila-1)
    palabra.posicion((fila, columna))


def generarPosicionVertical(palabra, dim_fila, dim_columna):
    """
        Funcion que genera la posicion de una palabra, para una grilla de Distribucion VERTICAL
        -> Recibe un Objeto Palabra
        -> Agrega un posicion al objetoPalabra: objeto.posicion(posicion)
    """
    len_palara = palabra.longitud
    columna = randint(0, dim_columna -1)
    fila = randint(0,dim_fila-(len_palabra))
    palabra.posicion((fila,columna))


def diccionarioPalabrasHorizontal(lista_palabras):
    """
        -> Recibe una lista con objPalabra
        -> Retorna una lista de objPalabras con su ubicacion respectiva en la grilla de direccion HORIZONTAL
    """
    lista_palabras_posicion = []
    fila, columna =  dimensionGrillaHorizontal(lista_palabras)
    lista_posiciones = []
    for palabra in lista_palabras:
        posicion_palabra = generarPosicionHorizontal(palabra, fila, columna)
        while palabra.posicion()[0] in lista_posiciones:
            posicion_palabra = generarPosicionHorizontal(palabra, fila, columna)
        lista_posicion.append(posicion_palabra[0])
        lista_palabras_posicion.append(palabra)
    return lista_palabras_posicion

def diccionarioPalabrasVertical(lista_palabras):
    """
        -> Recibe una lista con objPalabra
        -> Retorna una lista de objPalabras con su ubicacion respectiva en la grilla de direccion VERTICAL
    """
    lista_palabras_posicion =[]
    fila, columna = dimensionGrillaVertical(lista_palabras)
    lista_posicion =[]
    for palabra in lista_palabras:
        posicion_palabra = generarPosicionVertical(palabra, fila, columna)
        while(palabra.posicion()[0] in lista_posicion):
            posicion_palabra = generarPosicionVertical(palabra, fila, columna)
        lista_posicion.append(posicion_palabra[1])
        lista_palabras_posicion.append(palabra)
    return lista_palabras_posicion

def palabras_ordenadas_horizontal(lista_palabras):
    """
        -> Entrada lista de Objetos Palabras, cargadas con su posicion en una Grilla
        -> Retorna lista ordenada de  objetos Palabras, respecto a su posicion en FILA
    """
    lista_palabras_posicion = palabras_ordenadas_horizontal(lista_palabras)
    lista_ordenada = = sorted(lista_palabras_posicion, key = lambda palabra: palabra.posicion()[0])
    return lista_ordenada

def palabras_ordenadas_vertical(diccionario):
    """
        -> Entrada lista de Objetos Palabras, cargadas con su posicion en una Grilla
        -> Retorna lista ordenada de  objetos Palabras, respecto a su posicion en COLUMNA
    """
    lista_palabras_posicion = palabras_ordenadas_vertical(lista_palabras)
    lista_ordenada = = sorted(lista_palabras_posicion, key = lambda palabra: palabra.posicion()[1])
    return lista_ordenada
