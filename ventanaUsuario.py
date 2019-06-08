import os
import string
import random
import PySimpleGUI as sg
from collections import OrderedDict


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

palabras = OrderedDict()
palabras["ver"]= (3,2,1)
palabras["carro"]= (5,1,2)
palabras["bueno"]=(5,1,3)
#----------------------------------------------------------
def palabras_buscar(verbos=[], sustantivos=[], adjetivos=[]):
    #Retorna una lista con todos los tipos ingresados, esto nos servirar para alamcenar en la grilla
    return verbos + sustantivos + adjetivos

def elementos_fila(dim_fila, diccionario_palabras,i):
    #i = posicion de palabra, que coincide con el orde de columna
    #Retorna la fila cargada con la letra de las palabras, y letras aleatorias
    letras_fila = []
    lista_palabras = list(diccionario_palabras.keys())
    pos_fila = 0
    while pos_fila <= dim_fila:
        if(pos_fila == diccionario_palabras[lista_palabras[i]][1]):
            for letra in lista_palabras[i]:
                letras_fila.append(sg.Button(letra))
            pos_fila+= diccionario_palabras[lista_palabras[i]][0]
        else:
            letras_fila.append(sg.Button(letra_random()))
            pos_fila+=1
    return letras_fila


def generarGrillaHorizontal(dim_columna, dim_fila, diccionario_palabras):
    #Genera la grilla con las palabras contenidas en el diccionario,
    # el diccionario_palabras es de la forma: {palabra:(lenPalabra,fila, columna)} ordenadas ascendentemente respecto a la columna( utilizamos:from collections import OrderedDict)
    fila = []
    grilla_sopa_letras = []
    for columna in range(dim_columna):
        fila = elementos_fila(dim_fila, diccionario_palabras,columna)
        grilla_sopa_letras.append(fila)

    return grilla_sopa_letras

fila_de_palabras= elementos_fila(5,palabras,0)
print(fila_de_palabras)
print("-"*50)
print("-"*50)

grilla_Horizontal = generarGrillaHorizontal(3,5, palabras)
print(grilla_Horizontal)


layout = [
    [sg.Text('Sopa de letras', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('------------TABLAAA-------------', size=(35, 1))],
    [sg.Text('_' * 100, size=(70, 1))],

]


[layout.append(fillaGrilla) for fillaGrilla in  grilla_Horizontal]
# print(layout)
ventana= sg.Window('Grilla').Layout(layout)
while True:
    values = ventana.Read()
