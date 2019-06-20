import PySimpleGUI as sg
import elegirColores as ec
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from constantes import (
    TIPO_PALABRAS_CANT,
    AYUDA_COL,
    DIRECCION_COL,
    TAMANIO_COL,
)

from utilidades import *
from juego import Juego

AGREGAR = 'Agregar'
JUGAR = 'Jugar'


layout = [
    [sg.Text('Configuraciones', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
    [sg.Text('Ingrese una a una las palabras a encontrar')],
    [sg.InputText(), sg.ReadButton('Agregar')],
    [sg.Text('Elegir los colores para los tipos de palabras')],
    [sg.Button('Verbo',key='verb'), sg.Button('Sustantivo',key='noun'), sg.Button('Adjetivo',key='adjetive')],
    [sg.Column(AYUDA_COL)],
    [sg.Column(DIRECCION_COL)],
    [sg.Column(TIPO_PALABRAS_CANT)],
    [sg.Column(TAMANIO_COL)],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Tipografia')],  # TODO
    [sg.Text('Estilo')],  # TODO
    [sg.Text('Oficina')],  # TODO
    [sg.ReadButton('Jugar')],
]


window = sg.Window("Sopa de Letras").Layout(layout)

config = Configuracion()

dict_color = {}

while True:
    evento, valores = window.Read()
    if evento == 'Agregar':
        palabra = valores.get(2, None)  # en la pos 2 esta el valor del input
        palabra, definicion = Validacion.validar_con_wikcionario(palabra)
        if palabra:
            palabra = Palabra(palabra, definicion)
            config.agregar_palabras(palabra)
        else:
            # falta logica de generar reporte
            generar_reporte(palabra)
    elif evento == 'verb':
        color_select = ec.paleta_colores()
        dict_color['Verbo']=color_select
        print(dict_color)
    elif evento == 'noun':
        color_select = ec.paleta_colores()
        dict_color['Sustantivo']=color_select
        print(dict_color)
    elif evento == 'adjetive':
        color_select = ec.paleta_colores()
        dict_color['Adjetivo']=color_select
        print(dict_color)
    elif evento == JUGAR:
        config.seleccionar_palabras(valores)
        config.set_opciones(valores)
        valores.update({'opciones': config})
        window.Close()
        Juego.jugar(valores, config)
    elif evento is None:
        break
    window.Element(evento).Update(button_color=(('black',('blue',color_select)[True])))



window.Close()
