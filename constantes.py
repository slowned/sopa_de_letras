VERBOS = [
    'jugar',
    'llamar',
    'saltar',
    'correr',
    'buscar',
    'comer',
    'ver',
    'hablar',
]

ADJETIVOS = [
    'afortunado',
    'alto',
    'negro',
    'obsecuente',
    'paciente',
    'extremo',
    'famoso',
    'inteligente',
]

SUSTANTIVOS = [
    'animal',
    'libro',
    'aire',
    'esfera',
    'planta',
    'programa',
    'guitarra',
    'idea',
    'trabajo',
    'ciruela',
    'vaso',
]


LISTA_PALABRAS = VERBOS + ADJETIVOS + SUSTANTIVOS


MAXIMO_PALABRA = [x for x in range(10)]

import PySimpleGUI as sg
TIPO_PALABRAS_CANT = [
    [sg.Text('Verbos: ', background_color='#F7F3EC'), sg.Spin(values=MAXIMO_PALABRA, initial_value='0')],
    [sg.Text('Adjetivos: ', background_color='#F7F3EC'), sg.Spin(values=MAXIMO_PALABRA, initial_value='0')],
    [sg.Text('Sustantivos: ', background_color='#F7F3EC'), sg.Spin(values=MAXIMO_PALABRA, initial_value='0')],
    [sg.Text('Total:', background_color='#F7F3EC', justification='center', size=(10, 1))],
] 
