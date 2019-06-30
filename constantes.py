import string
import PySimpleGUI as sg
from utilidades import Palabra, Configuracion

from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE


MAXIMO_PALABRA = [x for x in range(10)]


LAYOUT_AYUDA = []
LAYOUT_JUEGO = [
    [sg.Text('Sopa de letras', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
]

# valores.get('opciones')
# config.




# ------- Elementos de opciones -------

AYUDA = "ayuda"
AYUDA_SI = "_ayuda_si_"
AYUDA_NO = "_ayuda_no_"
AYUDA_COL = [
    [sg.Text('Ayuda')],
    [sg.Radio('SI', "AYUDA", default=True, key=AYUDA_SI),
        sg.Radio('NO', "AYUDA", key=AYUDA_NO)],
]

DIRECCION = "direccion"
VERTICAL = "_vertical_si"
HORIZONTAL = "_vertical_no"
DIRECCION_COL = [
    [sg.Text('Orientacion Vertical/Horizontal')],
    [sg.Radio('VERTICAL', "DIRECCION", default=True, key=VERTICAL),
        sg.Radio('HORIZONTAL', "DIRECCION", key=HORIZONTAL)],
]

TAMANIO = "tamanio"
MAYUSCULA = "_tamanio_mayuscula_"
MINUSCULA = "_tamanio_minuscula_"
TAMANIO_COL = [
    [sg.Text('Mayuscula/Minuscula')],
    [sg.Radio('Mayusculas', "CAPS", default=True, key=MAYUSCULA),
        sg.Radio('Minusculas', "CAPS", key=MINUSCULA)],
]

TIPO_PALABRAS_CANT = [
    [sg.Text('Cantidad de palabras a mostrar (*)')],
    [sg.Text('Verbos: '),
        sg.Spin(values=MAXIMO_PALABRA, initial_value='0', key=VERB)],
    [sg.Text('Adjetivos: '),
        sg.Spin(values=MAXIMO_PALABRA, initial_value='0', key=ADJECTIVE)],
    [sg.Text('Sustantivos: '),
        sg.Spin(values=MAXIMO_PALABRA, initial_value='0', key=NOUN)],
]

# -------- Fin Elementos Opciones --------



VALORES = {
    0: '',  # input agregar palabra
    '_ayuda_si_': False,
    '_ayuda_no_': True,
    '_direccion_vertical_': False,
    '_direccion_orizontal_': True,
    'VB': '2',  # verbo
    'JJ': '2',  # adjetivo
    'NN': '0',  # sustantivo
    '_tamanio_mayuscula_': False,
    '_tamanio_minuscula_': True,
}

palabras = {
    NOUN: [],  # Sustantivo
    VERB: [],  # Verbo
    ADJECTIVE: [],  # Adjetivo
}

cantidad_palabras = {}
