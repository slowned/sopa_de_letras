import PySimpleGUI as sg 

def paleta_colores():
    COLORS = ['blue', 'green', 'red', 'yellow', 'lightblue', 'grey', 'pink','orange']

    sg.SetOptions(button_element_size=(12,1), element_padding=(0,0), auto_size_buttons=False, border_width=0)

    layout = [[sg.Text('Click on a color square to see both white and black text on that color', text_color='blue', font='Any 15')]]
    row = []
    layout = []
    # -- Create primary color viewer window --
    for rows in range(2):
        row = []
        for i in range(4):
            try:
                color = COLORS[rows+2*i]
                row.append(sg.Button(color, button_color=('black', color), key=color))
            except:
                pass
        layout.append(row)

    window = sg.Window('Color Viewer', grab_anywhere=False, font=('any 9')).Layout(layout)

    # -- Event loop --
    while True:
        event, values = window.Read()
        if event is None:
            break
        # -- Create a secondary window that shows white and black text on chosen color
        layout2 =[[sg.DummyButton(event, button_color=('white', event)), sg.DummyButton(event, button_color=('black', event))]]
        sg.Window('Buttons with white and black text', keep_on_top=True).Layout(layout2).Read(timeout=0)


#layout para elegir colores a los diferentes tipos de palabras!        

layout =[[sg.Button('Verbo'), sg.Button('Sustantivo'), sg.Button('Adjetivo')]]

window = sg.Window('Color', grab_anywhere=False, font=('any 9')).Layout(layout)

# -- Event loop --
while True:
    event, values = window.Read()
    if event is None:
        break
    if((event == 'Verbo') or (event == 'Sustantivo') or (event=="Adjetivo")):
        paleta_colores()
           
    