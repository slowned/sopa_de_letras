import PySimpleGUI as sg
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from constantes import ALFABETO
from utilidades import *


layout = [
    [sg.Input(size=(10, 1), do_not_clear=True, justification='right', key='input')],
    [
        sg.Button("a"),
        sg.Button("v"),
        sg.Button("e"),
        sg.Button("r"),
        sg.Button("p"),
        sg.Button("Sustantivo", button_color=('white', '#311380'), key=NOUN)
    ],  # primer fila
    [
        sg.Button("a"),
        sg.Button("h"),
        sg.Button("o"),
        sg.Button("l"),
        sg.Button("a"),
        sg.Button("Verbo", button_color=('white', '#007339'), key=VERB)
    ],  # segunda fila
    [
        sg.Button("b"),
        sg.Button("u"),
        sg.Button("e"),
        sg.Button("n"),
        sg.Button("o"),
        sg.Button("Adjetivo", button_color=('white', 'firebrick4'), key=ADJECTIVE)
    ],  # tercer fila
    [sg.Submit("Verificar"), sg.Button('Agregar', key="__agregar__")]
]

ventana = sg.Window("Esta es una ventana").Layout(layout)
abecedario = 'abcdefghijklmnopqrstuvwxyz'


palabra = ''
lista_key_palabras = [NOUN, VERB, ADJECTIVE]
palabras_juego = {VERB: [], NOUN: [], ADJECTIVE: []}




while True:
    event, values = ventana.Read()

    if event is None:
        break
    if event in lista_key_palabras:
        seleccionando = True
        palabra = ''
        tipo_palabra = event
    elif event in ALFABETO:
        print(event)
        letra = ventana.Element(event).ButtonText
        palabra += letra
        print("la palabra es: {}".format(palabra))
    elif event == '__agregar__':
        palabras_juego[tipo_palabra].append(palabra)
        palabra = ''
    elif event == '__verificar__':
        Validacion.ganar(confi.palabras, palabras_juego)

    print(palabras_juego)


ventana.Close()
