import PySimpleGUI as sg
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from .ubicacionDePalabra import (
        palabras_ordenadas_horizontal,
        palabras_ordenadas_vertical,
        dimensionGrillaVertical,
        dimensionGrillaHorizontal,
)

from .ventanaUsuario import (
        generarGrillaVertical,
        generarGrillaHorizontal,
)

from .utilidades import Validacion, Notificacion


from .constantes import LAYOUT_JUEGO
from .ventanaUsuario import BCOLOR, TEMPERATURA
from .opciones import *
import json


def generar_layout_ayuda(config):

    layout = []
    valores = ["AYUDA:"]
    if config.ayuda:
        #Ayuda Si: Muestra una ayuda completa
        for palabra in config.palabras:
            valor = 'palabra: {}, definicion: {}'.format(palabra.nombre, palabra.definicion)
            valores.append(valor)
    else:
        for palabra in config.palabras:
            valor = 'definicion: {}'.format(palabra.definicion)
            valores.append(valor)

    #layout.append(sg.Listbox(valores, size=(50, 5)))
    sg.Popup(valores)
    #return layout

def layout_instructivo():
    """
    Crear el layout de instrucciones
    """
    pass


class Juego():

    layout = LAYOUT_JUEGO
    columna_opciones = []
    lista_key_palabras = [NOUN, VERB, ADJECTIVE]
    palabras_juego = {VERB: [], NOUN: [], ADJECTIVE: []}

    action_keys = ['_verificar_', '_salir_']

    # TODO: crear metodo de clase para que habilite los tipo de palabras
    # y otro para que despinte de las letras cuando sale un popup de error

    @classmethod
    def habilitar_tipos(cls,ventana):
        for elemento in cls.lista_key_palabras:
            ventana.Element(elemento).Update(disabled=False)

    @classmethod
    def habilitar_acciones(cls, ventana):
        for elemento in cls.action_keys:
            ventana.Element(elemento).Update(disabled=False)

    @classmethod
    def habilitar_letras(cls, ventana, lista_letras):
        BCOLOR=('deep pink', 'peach puff')
        for letra in lista_letras:
            ventana.Element(letra).Update(button_color=BCOLOR)

    @classmethod
    def habilitar_todas_letras(cls,ventana,lista_all_letras):
        BCOLOR=('deep pink','peach puff')
        for letra in lista_all_letras:
           ventana.Element(letra).Update(button_color=BCOLOR)

    @classmethod
    def habilitar_ultima_palabra(cls,ventana,lista_palabra):
        BCOLOR=('deep pink','peach puff')
        for letra in lista_palabra:
           ventana.Element(letra).Update(button_color=BCOLOR)

    @classmethod
    def dibujar_botones(cls, config):
        cls.layout.append([sg.Button("SUSTANTIVO", button_color=('black',config.colores[NOUN]), size=(14,1), key=NOUN),
        sg.T(' ' * 1),sg.Button("VERBO", button_color=('black', config.colores[VERB] ),size=(14,1), key=VERB),
        sg.T(' ' * 1),sg.Button("ADJETIVO", button_color=('black', config.colores[ADJECTIVE] ),size=(14,1), key=ADJECTIVE)
        ])
    @classmethod
    def dibujar_excluir(cls):
        cls.columna_opciones.append([sg.T(' ' * 1)])
        cls.columna_opciones.append([sg.Button("ELIMINAR ULTIMA PALABRA", button_color=('black','green yellow'),size=(15,2), key='_clean_')])
        cls.columna_opciones.append([sg.Button("DESHACER", button_color=('black','SlateBlue2'),size=(15,1), key='_undo_'),sg.Button("LIMPIAR SOPA", button_color=('black','gold3'),size=(15,1), key='_undoall_')])

    @classmethod
    def instrucciones_ayuda(cls):
        cls.columna_opciones.append([sg.Button("INSTRUCCIONES", button_color=('black', 'indian red'),size=(15,1), key="_instructivo_"), sg.Submit("AYUDA",button_color=('black','SeaGreen2'),size=(15,1), key="_ayuda_")])

    @classmethod
    def dibujar(cls, grilla, config):
        cls.dibujar_botones(config)
        cls.dibujar_excluir()
        cls.instrucciones_ayuda()
        cls.layout.append([sg.T(' ')])
        [cls.layout.append(fila_grilla) for fila_grilla in grilla]
        cls.layout.append([sg.Submit("VERIFICAR", button_color=('white','black'),size=(14,2), key="_verificar_"),sg.T(' ' * 1), sg.Button('AGREGAR',button_color=('white','black'),size=(14,2), key="_agregar_"),sg.T(' ' * 1), sg.Button('SALIR', button_color=('white','black'),size=(8,2), key="_salir_"),sg.Column(cls.columna_opciones)])
        
    @classmethod
    def salir(cls, ventana):
        layout = [
            [sg.Button('Salir', key='salir_si'),
                # sg.Button('Cancelar', key='salir_no'),
                sg.Cancel(key='salir_no')]
        ]
        salir = sg.Window("salir del juego").Layout(layout)

        while True:
            event, values = salir.Read(timeout=0)
            if event == 'salir_si':
                return True, salir
            elif event == 'salir_no':
                return False, salir
            elif event is None:
                return False, salir

    @classmethod
    def jugar(cls, valores, config):  # Juego principal
        """
        Se encarga de instanciar la sopa de letras, dependiendo de las
        opciones seleccionadas, y controla el flujo del juego.
        """
        #agregamos el Layout titlo con la tipografia elegida
        cls.layout.append([sg.Text('SOPA DE LETRAS', size=(30, 1), font=("Arial", 25), text_color='dark slate gray')])
        # datos de temperatura para rapsberry
        if(config.json_datos):

            with open('datos_oficina.json.json', 'r') as file:
                oficinas = json.load(file)

            valores_temperatura = oficinas[config.oficina]
            suma_temperaturas = 0
            for  temperatura in valores_temperatura:
                suma_temperaturas += temperatura["temp"]

            promedio_temperatura = int(suma_temperaturas / len(valores_temperatura))

            for valor in TEMPERATURA_COLOR.keys():
                if promedio_temperatura in valor:
                    color_letra = TEMPERATURA_COLOR[valor]

                break

        else:
            color_letra = BCOLOR


        #TODO: agregarle +2 (columna y fila)
        # dibuja los layouts
        if config.direccion is True:  # direccion por defaul es vertical
            dimension_grilla = dimensionGrillaVertical(config.palabras)
            palabras_ord = palabras_ordenadas_vertical(config.palabras)
            grilla = generarGrillaVertical(dimension_grilla, palabras_ord, color_letra, config)
            cls.dibujar(grilla, config)
        else:
            dimension_grilla = dimensionGrillaHorizontal(config.palabras)
            palabras_ord = palabras_ordenadas_horizontal(config.palabras)
            grilla = generarGrillaHorizontal(dimension_grilla, palabras_ord, color_letra, config)
            cls.dibujar(grilla, config)

        ventana = sg.Window('Sopa de letras').Layout(cls.layout)
        rango = range(dimension_grilla[0]*dimension_grilla[1])

        config.keys = [str(e) for e in rango]

        generando = False
        hay_elemento = False
        no_es_vacio = False

        palabra = ''
        lista_letras_disabled = []
        letras_todas = []
        lista_palabra_ultima = []

        while True:
            print('pedir valores')
            evento, valores = ventana.Read()
            print(evento)
            if (evento is None):
                break
            # TODO: Agregar eventos ("clean_window", "clean_word")
            # seleccion de palabra
            if evento in cls.lista_key_palabras:    # Seleccion de verb, adj, sus
                #TODO: desactivar boton "salir" y "verificar"

                lista_key_disable = cls.lista_key_palabras[:]
                lista_key_disable.remove(evento)

                for elemento in lista_key_disable:
                    ventana.Element(elemento).Update(disabled=True)
                for elemento in cls.action_keys:
                    ventana.Element(elemento).Update(disabled=True)

                generando = True
                palabra = ''
                tipo_palabra = evento
            elif evento in config.keys and generando:
                # se va creando la palabra
                letra = ventana.Element(evento).ButtonText
                lista_letras_disabled.append(evento)
                letras_todas.append(evento)
                palabra += letra
                ventana.Element(evento).Update(button_color=(('black', ('red', config.colores[tipo_palabra])[True])))
            elif evento == '_agregar_':
                if palabra and tipo_palabra:
                    hay_elemento = True
                    no_es_vacio = True
                    ultima_palabra = palabra
                    ultimo_tipo = tipo_palabra
                    cls.palabras_juego[tipo_palabra].append(palabra.upper())
                    palabra = ''
                    cls.habilitar_tipos(ventana)
                    cls.habilitar_acciones(ventana)
                    lista_palabra_ultima = lista_letras_disabled
                    lista_letras_disabled = []
                else:
                    mensaje = ("Error", "Debe pintar una palabra antes de agregarla")
                    cls.habilitar_tipos(ventana)
                    Notificacion.aviso(mensaje)
            elif evento == '_verificar_':
                # TODO: dentro del pop up "ganaste/perdiste" agrerar 2 botones
                # volver a configuraciones, reintentar
                Validacion.ganar(config.palabras, cls.palabras_juego)
            elif evento == '_instructivo_':
                Notificacion.instrucciones()
            elif evento == '_ayuda_':
                generar_layout_ayuda(config)
            elif evento == '_undo_':
                cls.habilitar_tipos(ventana)
                cls.habilitar_letras(ventana,lista_letras_disabled)
                lista_letras_disabled=[]
            elif evento == '_undoall_':
                if no_es_vacio:
                    cls.habilitar_tipos(ventana)
                    cls.palabras_juego = {VERB: [], NOUN: [], ADJECTIVE: []}
                    cls.habilitar_todas_letras(ventana,letras_todas)
                    letras_todas = []
                    no_es_vacio = False
                    hay_elemento = False
                    print(cls.palabras_juego)
                else:
                    mensaje = ("Ups!","No hay nada que se pueda limpiar ;)")
                    cls.habilitar_tipos(ventana)
                    Notificacion.aviso(mensaje)
            elif evento == '_clean_':
                if hay_elemento:
                    cls.palabras_juego[ultimo_tipo].remove(ultima_palabra.upper())
                    print(cls.palabras_juego)
                    cls.habilitar_tipos(ventana)
                    cls.habilitar_ultima_palabra(ventana,lista_palabra_ultima)
                    lista_palabra_ultima = []
                    hay_elemento = False
                else:
                    mensaje = ("Ups!","No se ha agregado ninguna palabra :O")
                    cls.habilitar_tipos(ventana)
                    Notificacion.aviso(mensaje)
            elif evento is None:
                break
            elif evento == '_salir_':
                salir, vent = cls.salir(ventana)
                if salir is True:
                    vent.Close()
                    ventana.Close()
                else:
                    vent.Close()
                print('cancelo salir')

        ventana.Close()
