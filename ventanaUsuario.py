import os
import string
import random
import PySimpleGUI as sg


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
verbos = ["comimos","correr"]
sustantivos = ["profesor","niño"]
adjetivo =  ["amable","enorme"]
palabra = "correr"
#----------------------------------------------------------
def palabras_buscar(verbos=[], sustantivos=[], adjetivos=[]):
    #Retorna una lista con todos los tipos ingresados, esto nos servirar para alamcenar en la grilla
    return verbos + sustantivos + adjetivos

def elementos_fila(dim, diccionario_palabras):
    #Retorna la fila cargada con la letra de las palabras, y letras aleatorias
    letras_fila = []
    lista_palbras = list(diccionario_palabras.keys())
    while pos_fila <= dim:
        if(pos_fila ==diccionario_palabras(lista_palabras[i][1])):
            for letra in lista_palbras[i]:
                letras_fila.append(sg.Button(letra))
            fila+= diccionario_palabras(lista_palabras[i][0])
        else:
            letras_fila.append(sg.Button(letra_random()))
            pos_fila+=1
    return letras_fila

def generarGrillaHorizontal(dim, diccionario_palabras):
    #Genera la grilla con las palabras contenidas en el diccionario,
    # el diccionario_palabras es de la forma: {palabra:(lenPalabra,fila, columna)} ordenadas ascendentemente respecto a la columna( utilizamos:from collections import OrderedDict)
    fila = []
    grilla_sopa_letras = []
    for columna in range(dim):
        fila = elementos_fila(dim, diccionario_palabras)
        grilla.append(letra_fila)

    return grilla_sopa_letras

#create_grilla(10, palabra)
lista_palabras = ["correr", "reir"]
a= create_grilla(10,lista_palabras)
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

[layout.append(fillaGrilla) for fillaGrilla in  a]
# print(layout)
ventana= sg.Window('Grilla').Layout(layout)
while True:
    values = ventana.Read()
