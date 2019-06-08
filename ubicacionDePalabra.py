from collections import OrderedDict
from random import randint
"""
    Funciones para generar ubicacion aleatorio de las palabras
"""

#IMPORTANTE: REEMPLAZAR len(palabras) por: palabras.longitud
def dimensionGrillaHorizontal(lista_palabras):
    """
            Retorna la dimension de grilla para ubicar palabras HORIZONTALMENTE
    """
    dim_columna = 0
    dim_fila = len(lista_palabras)
    for palabra in lista_palabras:
        if(len(palabra) > dim_columna):
            dim_columna = len(palabra)
    return(dim_fila, dim_columna)

def dimensionGrillaVertical(lista_palabras):
    """
            Retorna la dimension de grilla para ubicar palabras VERTICALMENTE
    """
    # dim_columna = 0
    # dim_fila = len(lista_palabras)
    # for palabra in lista_palabras:
    #     if(len(palabra) > dim_columna):
    #         dim_columna = len(palabra)
    # return(dim_fila, dim_columna)
    columna, fila =dimensionGrillaHorizontal(lista_palabras)
    return(fila, columna)


def generarPosicionHorizontal(len_palabra,dim_fila, dim_columna):
    columna = randint(0, (dim_columna -len_palabra))
    fila = randint(0,dim_fila-1)
    return(fila, columna)


def generarPosicionVertical(len_palabra, dim_fila, dim_columna):
    columna = randint(0, dim_columna -1)
    fila = randint(0,dim_fila-(len_palabra))
    return(fila, columna)

# lista = ["ver","ser","reie","holamucndo"]
# a = generarPosicionHorizontal(9, 9, 4)
# print(a)

def diccionarioPalabrasHorizontal(lista_palabras):
    """
        Retorna una estructura de tipo dict: diccionario ={obj_palabra:(fila, columna)}, para ubicar la palabra HORIZONTALMENTE
    """
    diccionario_palabras = dict()
    lista_columna_asignadas = list(diccionario_palabras.values())
    fila, columna = dimensionGrillaHorizontal(lista_palabras)
    for palabra in lista_palabras:
        #len_palabra = len(palabra)
        len_palabra = len(palabra)
        posicion_palabra =generarPosicionHorizontal(len_palabra, fila, columna)
        while(posicion_palabra[0] in lista_columna_asignadas):
            posicion_palabra = generarPosicionHorizontal(len_palabra, fila, columna)
        lista_columna_asignadas.append(posicion_palabra[0])
        diccionario_palabras[palabra]=posicion_palabra
    return diccionario_palabras

def diccionarioPalabrasVertical(lista_palabras):
    """
        Retorna una estructura de tipo dict: diccionario ={obj_palabra:(fila, columna)}, para ubicar la palabra VERTICALMENTE
    """
    diccionario_palabras = dict()
    lista_fila_asignadas = list(diccionario_palabras.values())
    fila, columna = dimensionGrillaVertical(lista_palabras)
    for palabra in lista_palabras:
        len_palabra = len(palabra)
        posicion_palabra =generarPosicionVertical(len_palabra, fila, columna)
        while(posicion_palabra[1] in lista_fila_asignadas):
            posicion_palabra = generarPosicionVertical(len_palabra, fila, columna)
        lista_fila_asignadas.append(posicion_palabra[1])
        diccionario_palabras[palabra]=posicion_palabra
    return diccionario_palabras

def palabras_horizontal(diccionario):
    dic_palabras = OrderedDict()
    lista_items = diccionario.items()
    lista_ordenada = sorted(lista_items, key = lambda x : x[1][0])
    for elemento in lista_ordenada:
        dic_palabras[elemento[0]]=elemento[1]
    return dic_palabras

def palabras_vertical(diccionario):
    dic_palabras =OrderedDict()
    lista_items = diccionario.items()
    lista_ordenada = sorted(lista_items, key = lambda x : x[1][1])
    for elemento in lista_ordenada:
        dic_palabras[elemento[0]]=elemento[1]
    return dic_palabras

lista_palabras = ["ver", "correr", "comer", "carro", "celular", " nuevo"]
# print(dimensionGrillaHorizontal(lista_palabras))
# print(dimensionGrillaVertical(lista_palabras))
# print(generarPosicionHorizontal(len("celular"),6,7))
# print(generarPosicionVertical(len("celular"),7,6))
# print(diccionarioPalabrasHorizontal(lista_palabras))
# print(diccionarioPalabrasVertical(lista_palabras))
diccionario =diccionarioPalabrasVertical(lista_palabras)
print(palabras_horizontal(diccionario))
print(palabras_vertical(diccionario))

od = OrderedDict()
od['a'] = (1,4)
od['b'] = (2,4)
od['c'] = (3,1)
od['d'] = (4,7)
print(od['d'][1])
