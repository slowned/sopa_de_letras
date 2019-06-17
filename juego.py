import PySimpleGUI as sg
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



class Juego():
    layout = [
        [sg.Text('Sopa de letras', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
        [sg.Text('_' * 100, size=(70, 1))],
        [sg.Text('------------TABLAAA-------------', size=(35, 1))],
        [sg.Text('_' * 100, size=(70, 1))],
    ]

    @classmethod
    def dibujar(cls, grilla):
        [cls.layout.append(fila_grilla) for fila_grilla in grilla]
        ventana = sg.Window('Sopa le letras').Layout(cls.layout)
        while True:
            evento, valores = ventana.Read()
            if evento == None:
                break
        ventana.Close()

    @classmethod
    def jugar(cls, valores, config):
        if config.direccion is True:
            dimension_grilla = dimensionGrillaVertical(config.palabras)
            palabras_ord = palabras_ordenadas_vertical(config.palabras)
            grilla = generarGrillaVertical(dimension_grilla, palabras_ord)
            cls.dibujar(grilla)
        else:
            dimension_grilla = dimensionGrillaHorizontal(config.palabras)
            palabras_ord = palabras_ordenadas_horizontal(config.palabras)
            grilla = generarGrillaHorizontal(dimension_grilla, palabras_ord)
            cls.dibujar(grilla)


