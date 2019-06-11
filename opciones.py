import PySimpleGUI as sg
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from constantes import TIPO_PALABRAS_CANT


from utilidades import *

AGREGAR = 'Agregar'
JUGAR = 'Jugar'


layout = [
    [sg.Text('Configuraciones', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Ingrese una a una las palabras a encontrar')],
    [sg.InputText(), sg.ReadButton('Agregar')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Colores (sustantivos, adjetivos, verbos)')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Ayuda')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Orientacion Vertical/Horizontal')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Cantidad de palabras a mostrar')],
    [sg.Column(TIPO_PALABRAS_CANT, background_color='#F7F3EC')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Mayuscula/Minuscula')],
    [sg.Radio('Mayusculas', "caps", default=True), sg.Radio('Minusculas', "caps")],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Tipografia')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Estilo')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Oficina')],
    [sg.Text('_' * 100, size=(70, 2))],
    [sg.ReadButton('Jugar')],
]


window = sg.Window("Sopa de Letras").Layout(layout)

palabras = {
    NOUN: [],  # Sustantivo
    VERB: [],  # Verbo
    ADJECTIVE: [],  # Adjetivo
}

cantidad_palabras = {}

config = Configuracion()

while True:
    evento, valores = window.Read()
    if evento == 'Agregar':
        palabra = valores.get(2, None)  # en la pos 2 esta el valor del input
        palabra, definicion = Validacion.validar_con_wikcionario(palabra)
        if palabra:
            palabra = Palabra(palabra, definicion)
            config.agregar_palabra(palabra)
            # el tipo de la palabra lo genera la palabra
            # verificar con patters
        else:
            # falta logica de generar reporte
            generar_reporte(palabra)

    if evento == JUGAR:
        config.seleccionar_palabras(evento)
    if evento is None:
        break

window.Close()
