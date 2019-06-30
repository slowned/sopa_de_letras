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
        valor_palabra = valores.get(0, None)
        if valor_palabra:
            palabra, definicion = Validacion.validar_con_wikcionario(valor_palabra)
            if palabra:
                palabra = Palabra(palabra, definicion)
                config.agregar_palabras(palabra)
                mensaje = ("Exito", "la palabra {}, se agrego con exito".format(palabra))
                Notificacion.aviso(mensaje)
            else:
                Notificacion.generar_reporte(valor_palabra)
                mensaje = ("Palabra inexistente",
                           "No se pudo validar la palabra, fue agregada al reporte")
                Notificacion.aviso(mensaje)
        else:
            mensaje = (("Campo vacio", "debe agregar palabras para jugar"))
            Notificacion.aviso(mensaje)


    elif evento == 'verb':
        color_select = ec.paleta_colores()
        config.agregar_color(NOUN, color_select)

    elif evento == 'noun':
        color_select = ec.paleta_colores()
        config.agregar_color(NOUN, color_select)

    elif evento == 'adjetive':
        color_select = ec.paleta_colores()
        config.agregar_color(ADJECTIVE, color_select)

    elif evento == JUGAR:
        print(valores)
        if Validacion.verificar_colores(dict_color):
            if Validacion.verificar_cantidad_palabras(valores):
                config.seleccionar_palabras(valores)
                config.set_opciones(valores)
                valores.update({'opciones': config})
                window.Close()
                Juego.jugar(valores, config)
            else:
                mensaje = ("Campo obligatorio: Cantidad de palabras", "Tenes que seleccionar una cantidad minima de palabras para poder encontrarlas")
                Notificacion.aviso(mensaje)
        else:
            mensaje = ("Campo obligatorio: Colores", "Asocia un color a un tipo de palabra, ejemplo: selecciona sustantivo y asignale el color amarillo")
            Notificacion.aviso(mensaje)
    elif evento is None:
        break

    # window.Element(evento).Update(button_color=(('black',('blue',color_select)[True])))

    # TODO: si esto esta aca cuando se pone jugar
    # y no se seleccionaron colores rompe,
    # deberia estar en el metodo donde se asignan los colores
    # en ec.paleta_colores()



window.Close()
