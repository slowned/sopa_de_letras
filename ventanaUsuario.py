import os
import string
import random
import PySimpleGUI as sg
from collections import OrderedDict
from utilidades import *


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



def elementos_fila(dim_columna, diccionario_palabras,i):

    letras_fila = []
    lista_palabras = list(diccionario_palabras.keys())
    pos_columna = 0
    while pos_columna <= dim_columna:
        if(pos_columna == diccionario_palabras[lista_palabras[i]][1]):
            for letra in lista_palabras[i]:
                letras_fila.append(sg.Button(letra))
            pos_columna+= diccionario_palabras[lista_palabras[i]][0]
        else:
            letras_fila.append(sg.Button(letra_random()))
            pos_columna+=1
    return letras_fila

def elementos_columna(dim_fila, diccionario_palabras,i):

    letra_columna = []
    lista_palabras = list(diccionario_palabras.keys())
    pos_fila = 0
    while pos_fila <= dim_fila:
        if(pos_fila == diccionario_palabras[lista_palabras[i]][1]):
            for letra in lista_palabras[i]:
                letra_columna.append(sg.Button(letra))
            pos_fila+= diccionario_palabras[lista_palabras[i]][0]
        else:
            letra_columna.append(sg.Button(letra_random()))
            pos_fila+=1
    return letra_columna


def generarGrillaHorizontal(dimension_grilla, diccionario_palabras):
    """
        Entrada:
                Dimension de la grilla: (dim_fila, dim_columna)
                Diccionario ordenado de palabras : {palabra:(fila, columna)}
        Salida: Grilla
    """
    dim_fila, dim_columna = dimension_grilla
    fila_sopa = []
    grilla_sopa_letras = []

    for fila in range(dim_fila):
        fila_sopa = elementos_fila(dim_columna, diccionario_palabras,fila)
        grilla_sopa_letras.append(fila_sopa)

    return grilla_sopa_letras

def generarGrillaVertical(dimension_grilla, diccionario_palabras):
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
        columna_sopa = elementos_columna(dim_fila, diccionario_palabras,columna)
        grilla_sopa_letras.append(columna_sopa)

    return grilla_sopa_letras


layout = [
    [sg.Text('Sopa de letras', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('------------TABLAAA-------------', size=(35, 1))],
    [sg.Text('_' * 100, size=(70, 1))],
# [sg.Button('Customized', button_color=('white', 'green')),sg.Button('Customized', button_color=('white', 'green'))]
    #[create_grilla()],
]
# print(a)
# print("-"*50)

[layout.append(fillaGrilla) for fillaGrilla in  grilla_Horizontal]
# print(layout)
ventana= sg.Window('Grilla').Layout(layout)
while True:
    values = ventana.Read()
