import os
import string
import random
import PySimpleGUI as sg
from utilidades import *

"""
Ventana de Usuario
    -> Muestra:
                <=> Grilla ( HORIZONTAL / VERTICAL)
                <=> Ayuda (SI /NO)
                <=> Verificacion
"""

def letra_random(mayuscula=False):
    """
        retorna una letra al azar:
                si mayuscula = Flase-> return minuscula
                su mayuscula = True -> return mayuscula
    """
    alfabero = string.ascii_letters
    letra = random.choice(alfabero)
    if(not mayuscula):
        return letra.lower()
    else:
        return letra.upper()

def crear_boton():
    btn = [sg.Button(letra_random(), button_color=('white', 'green'))]
    return btn


#_________________________________________________________
"""
A continuacion se presentan valores hardcodeados de:
    verbos, sustantivos, adjetivos
servira para comenzar a ubicar las palabras en la grilla
"""
# verbos = ["comimos","correr"]
# sustantivos = ["profesor","niño"]
# adjetivo =  ["amable","enorme"]
# palabra = "correr"
# palabras["ver"]= (3,2,1)
# palabras["carro"]= (5,1,2)
# palabras["bueno"]=(5,1,3)
#----------------------------------------------------------

def elementos_fila(dim_columna,fila_palabra, palabra):
    letras_fila = []
    pos_columna = 0
    add = 0
    while pos_columna <= dim_columna:
        key_letra = dim_columna * fila_palabra + add
        if(pos_columna == palabra.posicion[1]):
            for letra in palabra.nombre:
                letras_fila.append(sg.Button(letra, key=key_letra))
            #pos_columna+= diccionario_palabras[lista_palabras[i]][0]
            pos_columna +=palabra.longitud
            add+=1
        else:
            letras_fila.append(sg.Button(letra_random(),key=key_letra))
            pos_columna+=1
            add+=1
    return letras_fila


def elementos_columna(dim_fila,columna_palabra palabra):
    letra_columna = []
    pos_fila = 0
    add=0
    while pos_fila <= dim_fila:
        key_letra = dim_columna * fila_palabra + add
        if(pos_fila == palabra.posicion[1]):
            for letra in palabra.nombre:
                letra_columna.append(sg.Button(letra), key=key_letra)
                add+=1
            pos_fila+= palabra.longitud
        else:
            letra_columna.append(sg.Button(letra_random(), key=key_letra))
            pos_fila+=1
            add+=1
    return letra_columna


def generarGrillaHorizontal(dimension_grilla, lista_palabras):
    """
        Entrada:
                Dimension de la grilla: (dim_fila, dim_columna)
                Lista ordenada de obj Palabras
        Salida: Grilla
    """
    dim_fila, dim_columna = dimension_grilla
    fila_grilla = []
    grilla_sopa_letras = []
    for fila in range(dim_fila):
        fila_grilla = elementos_fila(dim_columna,fila, lista_palabras[fila])
        grilla_sopa_letras.append(fila_grilla)

    return grilla_sopa_letras

def generarGrillaVertical(dimension_grilla, lista_palabras):
    """
        Entrada:
                Dimension de la grilla: (dim_fila, dim_columna)
                Diccionario ordenado de palabras : {palabra:(fila, columna)}
        Salida: Grilla
    """
    dim_fila, dim_columna = dimension_grilla
    columna_sopa = []
    grilla_sopa_letras = []
    for columna in range(dim_columna):
        columna_sopa = elementos_columna(dim_fila,columna, lista_palabras[columna])
        grilla_sopa_letras.append(columna_sopa)

    return grilla_sopa_letras
