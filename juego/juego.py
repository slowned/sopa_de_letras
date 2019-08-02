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
        cls.columna_opciones.append([sg.Button("DESHACER", button_color=('black','LightBlue1'), key='UNDO'),])

    @classmethod
    def instrucciones_ayuda(cls):
        cls.columna_opciones.append([sg.Button("INSTRUCCIONES", button_color=('black', 'indian red'), key="_instructivo_"), sg.Submit("AYUDA", key="_ayuda_")])

    @classmethod
    def dibujar(cls, grilla, config):
        cls.dibujar_botones(config)
        cls.dibujar_excluir()
        cls.instrucciones_ayuda()
        [cls.layout.append(fila_grilla)for fila_grilla in grilla]
        cls.layout.append([sg.Submit("Verificar", key="_verificar_"), sg.Button('Agregar', key="_agregar_"), sg.Button('Salir', key="_salir_"),sg.Column(cls.columna_opciones)])

    @classmethod
    def jugar(cls, valores, config):  #Juego principal
        """
        Se encarga de instanciar la sopa de letras, dependiendo de las
        opciones seleccionadas, y controla el flujo del juego.
        """
        #agregamos el Layout titlo con la tipografia elegida
        cls.layout.append([sg.Text('Sopa de letras', size=(30, 1), font=config.tipografia_titulo , text_color='blue')])
        # datos de temperatura para rapsberry
        if(config.json_datos):

            with open('datos_oficina.json.json','r') as file:
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

        ventana = sg.Window('Sopa le letras').Layout(cls.layout)
        rango = range(dimension_grilla[0]*dimension_grilla[1])

        config.keys = [str(e) for e in rango]

        generando = False

        palabra = ''
        lista_letras_disabled = []

        while True:
            evento, valores = ventana.Read()
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
                generando = True
                palabra = ''
                tipo_palabra = evento
            elif evento in config.keys and generando:
                # se va creando la palabra
                letra = ventana.Element(evento).ButtonText
                lista_letras_disabled.append(evento)
                palabra += letra
                ventana.Element(evento).Update(button_color=(('white', ('red', config.colores[tipo_palabra])[True])))
            elif evento == '_agregar_':
                if palabra and tipo_palabra:
                    cls.palabras_juego[tipo_palabra].append(palabra.upper())
                    palabra = ''
                    cls.habilitar_tipos(ventana)
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
            elif evento == 'UNDO':
                cls.habilitar_tipos(ventana)
                cls.habilitar_letras(ventana,lista_letras_disabled)
                lista_letra_disabled=[]
            elif evento == '_salir_':
                # TODO PopUP estas seguro?
                ventana.Close()
        ventana.Close()
