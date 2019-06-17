import PySimpleGUI as sg
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from ubicacionDePalabra import (
        palabras_ordenadas_horizontal,
        palabras_ordenadas_vertical,
        dimensionGrillaVertical,
        dimensionGrillaHorizontal,
)

from ventanaUsuario import (
        generarGrillaVertical,
        generarGrillaHorizontal,
)

from utilidades import Validacion


from constantes import LAYOUT_JUEGO


def generar_layout_ayuda(config):
    layout = []
    valores = []
    for palabra in config.palabras:
        valor = 'palabra: {}, definicion: {}'.format(palabra.nombre, palabra.definicion)
        valores.append(valor)

    layout.append(sg.Listbox(valores, size=(50, 5)))
    return layout


class Juego():

    layout = LAYOUT_JUEGO
    lista_key_palabras = [NOUN, VERB, ADJECTIVE]
    palabras_juego = {VERB: [], NOUN: [], ADJECTIVE: []}

    @classmethod
    def dibujar(cls, grilla, config):
        [cls.layout.append(fila_grilla) for fila_grilla in grilla]
        if config.ayuda:
            [cls.layout.append(generar_layout_ayuda(config))]
        cls.layout.append([sg.Submit("Verificar", key="_verificar_"), sg.Button('Agregar', key="_agregar_")])

    @classmethod
    def jugar(cls, valores, config):
        if config.direccion is True:
            dimension_grilla = dimensionGrillaVertical(config.palabras)
            palabras_ord = palabras_ordenadas_vertical(config.palabras)
            grilla = generarGrillaVertical(dimension_grilla, palabras_ord)
            cls.dibujar(grilla, config)
        else:
            dimension_grilla = dimensionGrillaHorizontal(config.palabras)
            palabras_ord = palabras_ordenadas_horizontal(config.palabras)
            grilla = generarGrillaHorizontal(dimension_grilla, palabras_ord)
            cls.dibujar(grilla, config)

        ventana = sg.Window('Sopa le letras').Layout(cls.layout)

        while True:
            evento, valores = ventana.Read()
            if evento is None:
                break
            if evento in cls.lista_key_palabras:
                tipo_palabra = evento
                palabra = ''
                lista_key_disable = cls.lista_key_palabras[:]
                lista_key_disable.remove(evento)
                for elemento in lista_key_disable:
                    ventana.Element(elemento).Update(disabled=True)
            elif evento in config.keys:
                letra = ventana.Element(evento).ButtonText
                palabra += letra
                ventana.Element(evento).Update(button_color=(('white', ('red','blue')[True])))
            elif evento == '_agregar_':
                cls.palabras_juego[tipo_palabra].append(palabra)
                palabra = ''
                for elemento in lista_key_disable:
                    ventana.Element(elemento).Update(disabled=False)
            elif evento == '_verificar_':
                Validacion.ganar(conf.palabras, cls.palabras_juego)







        ventana.Close()


