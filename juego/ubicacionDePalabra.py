from random import randint
from .utilidades import *

"""
    - Funciones para generar ubicacion aleatorio de las palabras
    - Recibimos una Lista con las palabras listas para cargar en la Grilla
"""


def dimensionGrillaHorizontal(lista_palabras):
    """
            ->Recibe una Lista de Objeto palabras
            ->Retorna la dimension de grilla para ubicar palabras HORIZONTALMENTE
    """
    dim_columna = 0
    dim_fila = len(lista_palabras)
    for palabra in lista_palabras:
        if palabra.longitud > dim_columna:
            dim_columna = palabra.longitud
    return(dim_fila, dim_columna)


def dimensionGrillaVertical(lista_palabras):
    """
                ->Recibe una Lista de Objeto palabras
                ->Retorna la dimension de grilla para ubicar palabras VERTICALMENTE
    """
    dim_fila = 0
    dim_columna = len(lista_palabras)
    for palabra in lista_palabras:
        if palabra.longitud > dim_fila:
            dim_fila = palabra.longitud
    return(dim_fila, dim_columna)


def generarPosicionHorizontal(palabra, dim_fila, dim_columna):
    """
        Funcion que genera la posicion de una palabra, para una grilla de Distribucion HORIZONTAL
        -> Recibe un Objeto Palabra
        -> Agrega un posicion al objetoPalabra: objeto.posicion(posicion)
    """
    len_palabra = palabra.longitud
    columna = randint(0, (dim_columna - len_palabra))
    fila = randint(0, dim_fila-1)
    palabra.posicion = (fila, columna)


def generarPosicionVertical(palabra, dim_fila, dim_columna):
    """
        Funcion que genera la posicion de una palabra, para una grilla de Distribucion VERTICAL
        -> Recibe un Objeto Palabra
        -> Agrega un posicion al objetoPalabra: objeto.posicion(posicion)
    """
    len_palabra = palabra.longitud
    columna = randint(0, dim_columna - 1)
    fila = randint(0, dim_fila - (len_palabra))
    palabra.posicion = (fila, columna)


def listaPalabrasHorizontal(lista_palabras):
    """
        -> Recibe una lista con objPalabra
        -> Retorna una lista de objPalabras con su ubicacion respectiva en la grilla de direccion HORIZONTAL
    """
    lista_palabras_posicion = []
    fila, columna=  dimensionGrillaHorizontal(lista_palabras)
    lista_posicion = []
    for palabra in lista_palabras:
        generarPosicionHorizontal(palabra, fila, columna)
        posicion_palabra = palabra.posicion
        while palabra.posicion[0] in lista_posicion:
            generarPosicionHorizontal(palabra, fila, columna)
            posicion_palabra = palabra.posicion
        lista_posicion.append(posicion_palabra[0])
        lista_palabras_posicion.append(palabra)
    return lista_palabras_posicion


# def listaPalabrasVertical(lista_palabras):
#     """
#         -> Recibe una lista con objPalabra
#         -> Retorna una lista de objPalabras con su ubicacion respectiva en la grilla de direccion VERTICAL
#     """
#     lista_palabras_posicion = []
#     # fila, columna = dimensionGrillaVertical(lista_palabras)(creo q aqui es al reves)
#     fila, columna= dimensionGrillaVertical(lista_palabras)
#     lista_posicion = []
#     for palabra in lista_palabras:
#         generarPosicionVertical(palabra, fila, columna)
#         posicion_palabra = palabra.posicion
#         while palabra.posicion[1] in lista_posicion:
#             generarPosicionVertical(palabra, fila, columna)
#             posicion_palabra = palabra.posicion
#         lista_posicion.append(posicion_palabra[1])
#         lista_palabras_posicion.append(palabra)
#     return lista_palabras_posicion
def listaPalabrasVertical(lista_palabras):
    """
        -> Recibe una lista con objPalabra
        -> Retorna una lista de objPalabras con su ubicacion respectiva en la grilla de direccion VERTICAL
    """
    lista_palabras_posicion = []
    fila, columna = dimensionGrillaVertical(lista_palabras)
    posicion_vertical = []
    for palabra in lista_palabras:
        generarPosicionVertical(palabra, fila, columna)
        posicion_palabra = palabra.posicion
        if posicion_palabra[1] in posicion_vertical:
            while palabra.posicion[1] in posicion_vertical:
                generarPosicionVertical(palabra, fila, columna)
            #posicion_palabra = palabra.posicion
            posicion_vertical.append(palabra.posicion[1])
        else:
            posicion_vertical.append(palabra.posicion[1])

        lista_palabras_posicion.append(palabra)

    return lista_palabras_posicion


def palabras_ordenadas_horizontal(lista_palabras):
    """
        -> Entrada lista de Objetos Palabras, cargadas con su posicion en una Grilla
        -> Retorna lista ordenada de  objetos Palabras, respecto a su posicion en FILA
    """
    lista_palabras_posicion = listaPalabrasHorizontal(lista_palabras)
    lista_ordenada = sorted(lista_palabras_posicion,
                            key=lambda palabra: palabra.posicion[0])
    return lista_ordenada


def palabras_ordenadas_vertical(lista_palabras):
    """
        -> Entrada lista de Objetos Palabras, cargadas con su posicion en una Grilla
        -> Retorna lista ordenada de  objetos Palabras, respecto a su posicion en COLUMNA
    """
    lista_palabras_posicion = listaPalabrasVertical(lista_palabras)
    lista_ordenada = sorted(lista_palabras_posicion,
                            key=lambda palabra: palabra.posicion[1])
    return lista_ordenada
