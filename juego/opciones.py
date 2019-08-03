import PySimpleGUI as sg
from juego.elegirColores import paleta_colores
from juego.tipografia import tipo_letra
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from juego.constantes import (
    TIPO_PALABRAS_CANT,
    AYUDA_COL,
    DIRECCION_COL,
    TAMANIO_COL,
    OFICINAS_COL,
    DIRECCION_COL,
)
from .utilidades import PALABRAS_TODAS

from .utilidades import *
from juego.juego import Juego

__all__ = ['Opcion']


class Opcion():
    @classmethod
    def opciones(cls):
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
            [sg.Column(DIRECCION_COL)],
            [sg.Button('Tipografia Título', key = '__titulo__')],
            [sg.Button('Tipografia Texto', key = '__texto__')],  # TODO titulo y texto
            [sg.Text('Estilo')],  # TODO
            [sg.Column(OFICINAS_COL)],  # TODO
            [sg.ReadButton('Jugar')],
        ]


        window = sg.Window("Sopa de Letras").Layout(layout)

        config = Configuracion()

#dict_color = {}


        while True:
            evento, valores = window.Read()
            if evento == 'Agregar':
                valor_palabra = valores.get(0, None)
                if valor_palabra:
                    #   TODO: cambiar libreria wikictionario(patters)
                    #   comparar con patters
                    palabra, definicion = Validacion.validar_con_wikcionario(valor_palabra)
                    if palabra:
                        palabra = Palabra(palabra, definicion)
                        config.agregar_palabras(palabra)
                        mensaje = ("Exito", "la palabra {}, se agrego con exito".format(palabra))
                        Notificacion.aviso(mensaje)
                    else:
                        # TODO: agrega palabra y diferencia con patter
                        Notificacion.generar_reporte(valor_palabra)
                        mensaje = ("Palabra inexistente",
                                   "No se pudo validar la palabra, fue agregada al reporte")
                        Notificacion.aviso(mensaje)
                else:
                    mensaje = (("Campo vacio", "debe agregar palabras para jugar"))
                    Notificacion.aviso(mensaje)


            elif evento == 'verb':
                color_select = paleta_colores()
                if not(Validacion.validar_color_usado(color_select, config.colores.values())):
                    config.agregar_color(VERB, color_select)
                    window.Element(evento).Update(button_color=(('black',('blue',color_select)[True])))
                else:
                    mensaje =("Error"," El color fue seleccionado")
                    Notificacion.aviso(mensaje)


            elif evento == 'noun':
                color_select = paleta_colores()
                if not(Validacion.validar_color_usado(color_select, config.colores.values())):
                    config.agregar_color(NOUN, color_select)
                    window.Element(evento).Update(button_color=(('black',('blue',color_select)[True])))
                else:
                    mensaje =("Error"," El color fue seleccionado")
                    Notificacion.aviso(mensaje)


            elif evento == 'adjetive':
                color_select = paleta_colores()
                if not(Validacion.validar_color_usado(color_select, config.colores.values())):
                    config.agregar_color(ADJECTIVE, color_select)
                    window.Element(evento).Update(button_color=(('black',('blue',color_select)[True])))
                else:
                    mensaje =("Error"," El color fue seleccionado")
                    Notificacion.aviso(mensaje)

            #-----Agregamos Tipografia
            elif evento == '__titulo__':
                t_titulo = tipo_letra("Titulo")
                print(t_titulo)

            elif evento == '__texto__':
                t_texto = tipo_letra("Texto")
                print(t_texto)


            elif evento == JUGAR:
                if Validacion.verificar_colores(config.colores):
                    if Validacion.verificar_cantidad_palabras(valores):
                        config.set_opciones(valores)
                        config.seleccionar_palabras(valores)
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



        window.Close()
