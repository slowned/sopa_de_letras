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

from utilidades import Validacion, Notificacion


from constantes import LAYOUT_JUEGO


def generar_layout_ayuda(config):
    """
    Crear el layout de ayuda, con las palabras y sus definiciones
    """
    layout = []
    valores = []
    for palabra in config.palabras:
        valor = 'palabra: {}, definicion: {}'.format(palabra.nombre, palabra.definicion)
        valores.append(valor)

    layout.append(sg.Listbox(valores, size=(50, 5)))
    return layout

def layout_instructivo():
    #TODO: popUp con instrucciones de Juego
        #
    pass



class Juego():

    layout = LAYOUT_JUEGO
    lista_key_palabras = [NOUN, VERB, ADJECTIVE]
    palabras_juego = {VERB: [], NOUN: [], ADJECTIVE: []}

    # TODO: crear metodo de clase para que habilite los tipo de palabras
    # y otro para que despinte de las letras cuando sale un popup de error

    @classmethod
    def habilitar_tipos(cls,ventana):
        for elemento in cls.lista_key_palabras:
            ventana.Element(elemento).Update(disabled=False)

    @classmethod
    def habilitar_letras(cls,ventana,lista_letras):
        BCOLOR=('deep pink','peach puff')
        for letra in lista_letras:
            ventana.Element(letra).Update(button_color=BCOLOR)

    @classmethod
    def dibujar_botones(cls, config):
        cls.layout.append([sg.Button("SUSTANTIVO", button_color=('white',config.colores[NOUN]), key=NOUN),
        sg.Button("VERBO", button_color=('white', config.colores[VERB] ), key=VERB),
        sg.Button("ADJETIVO", button_color=('white', config.colores[ADJECTIVE] ), key=ADJECTIVE)
        ])

    @classmethod
    def dibujar_excluir(cls):
        cls.layout.append([sg.Button("DESHACER", button_color=('white','LightBlue1'), key='UNDO'),])


    @classmethod
    def dibujar(cls, grilla, config):
        cls.dibujar_botones(config)
        cls.dibujar_excluir()
        cls.layout.append([sg.Submit("Instruccion de Juego", key= "_instrcciones_")])
        [cls.layout.append(fila_grilla) for fila_grilla in grilla]
        if config.ayuda:
            [cls.layout.append(generar_layout_ayuda(config))]
        cls.layout.append([sg.Submit("Verificar", key="_verificar_"), sg.Button('Agregar', key="_agregar_")])


    @classmethod
    def jugar(cls, valores, config):  #Juego principal
        if config.direccion is True:  # direccion por defaul es vertical
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
        rango = range(dimension_grilla[0]*dimension_grilla[1])

        config.keys = [str(e) for e in rango]

        generando = False

        palabra = ''
        lista_letras_disabled=[]

        while True:
            evento, valores = ventana.Read()
            if evento is None:
                break
            if evento in cls.lista_key_palabras:    # Seleccion de verb, adj, sus
                lista_key_disable = cls.lista_key_palabras[:]
                lista_key_disable.remove(evento)
                for elemento in lista_key_disable:
                    ventana.Element(elemento).Update(disabled=True)
                generando = True
                palabra = ''
                tipo_palabra = evento
            elif evento in config.keys and generando:
                letra = ventana.Element(evento).ButtonText
                lista_letras_disabled.append(evento)
                palabra += letra
                ventana.Element(evento).Update(button_color=(('white', ('red', 'blue')[True])))
            elif evento == '_agregar_':
                if palabra and tipo_palabra:
                    cls.palabras_juego[tipo_palabra].append(palabra)
                    palabra = ''
                    for elemento in lista_key_disable:
                        ventana.Element(elemento).Update(disabled=False)
                else:
                    mensaje = ("Error", "Debe pintar una palabra antes de agregarla")
                    # TODO: volver a activar todos los botones.. letras y tipo
                    Notificacion.aviso(mensaje)

            elif evento == '_verificar_':
                Validacion.ganar(config.palabras, cls.palabras_juego)
            elif evento == '_instrcciones_':
                # TODO: generar logica de las intrucciones
                # Dentro de la clase notificaciones
                layout_instructivo()
            elif evento == 'UNDO':
                cls.habilitar_tipos(ventana)
                cls.habilitar_letras(ventana,lista_letras_disabled)
                lista_letra_disabled=[]
        ventana.Close()
