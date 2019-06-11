from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE


MAXIMO_PALABRA = [x for x in range(10)]

import PySimpleGUI as sg
TIPO_PALABRAS_CANT = [
    [sg.Text('Verbos: ', background_color='#F7F3EC'), sg.Spin(values=MAXIMO_PALABRA, initial_value='0', key=VERB)],
    [sg.Text('Adjetivos: ', background_color='#F7F3EC'), sg.Spin(values=MAXIMO_PALABRA, initial_value='0', key=ADJECTIVE)],
    [sg.Text('Sustantivos: ', background_color='#F7F3EC'), sg.Spin(values=MAXIMO_PALABRA, initial_value='0', key=NOUN)],
    [sg.Text('Total:', background_color='#F7F3EC', justification='center', size=(10, 1))],
]

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


PALABRAS_TODAS = {VERB: VERBOS, ADJECTIVE: ADJETIVOS, NOUN: SUSTANTIVOS}
