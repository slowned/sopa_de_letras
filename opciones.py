import PySimpleGUI as sg
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
    [sg.Text('Colores (sustantivos, adjetivos, verbos)')],  # Juan
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

    if evento == JUGAR:
        config.seleccionar_palabras(valores)
        config.set_opciones(valores)
        valores.update({'opciones': config})
        window.Close()
        Juego.jugar(valores, config)

    if evento is None:
        break


window.Close()
