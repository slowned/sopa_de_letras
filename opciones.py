import PySimpleGUI as sg

from utilidades import *

config = Configuracion()

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
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Mayuscula/Minuscula')],
    [sg.Radio('Mayusculas', "caps", default=True), sg.Radio('Minusculas', "caps")],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Tipografia')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Estilo')],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('Oficina')],
    [sg.Text('_' * 100, size=(70, 1))],
]


window = sg.Window("Sopa de Letras").Layout(layout)


while True:
    evento, valores = window.Read()
    if(evento == 'Agregar'):
        palabra = valores.get(2, None)  # en la pos 2 esta el valor del input
        palabra, definicion = Validacion.validar_con_wikcionario(palabra)
        if palabra:
            palabra = Palabra(palabra, definicion)
            config.agregar_palabra(palabra)
            # verificar con paters y agregar el tipo
        else:
            generar_reporte(palabra)
