import PySimpleGUI as sg

def tipo_letra(ubicacion):
    """
        Funcion que retorna la tipografía elegida
        input : ubicacion( titulo o cuerpo)
        return : (tipografia_titulo, tamaño_titulo)
    """
    layout =[
            [sg.Text(ubicacion, font=("Helvetica", 15))],
            [sg.InputCombo(('Helvetica', 'Any'), size=(20, 1))],
            [sg.InputCombo((12,14,16,18,20,22,24,26), size=(20, 1))],
            [sg.Submit("OK")]
            ]

    window = sg.Window('').Layout(layout)
    while True:
        event, valores = window.Read()
        if event is None:
            break
        if event is "OK":
            window.Close()
            return tuple(valores.values())
