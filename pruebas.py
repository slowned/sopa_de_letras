import PySimpleGUI as sg
layout = [
    [sg.ReadButton("a"),sg.ReadButton("v"), sg.ReadButton("e"),sg.ReadButton("r"),sg.ReadButton("p"),  sg.Button("Sustantivo",button_color=('white','#311380'), key = '_NOUN_' )],
    [sg.ReadButton("a"),sg.ReadButton("h"), sg.ReadButton("o"),sg.ReadButton("l"),sg.ReadButton("a"), sg.Button("Verbo", button_color=('white','#007339'), key ='_VER_')],
    [sg.ReadButton("b"),sg.ReadButton("u"), sg.ReadButton("e"),sg.ReadButton("n"),sg.ReadButton("o"),  sg.Button("Adjetivo", button_color=('white','firebrick4'), key = '_ADJETIVE_')],
    [sg.Submit("Verificar"), sg.Button('OK')]
    ]
ventana = sg.Window("Esta es una ventana").Layout(layout)
abecedario = 'abcdefghijklmnopqrstuvwxyz'
while True:
    event, value = ventana.Read()
    lista_tipo_palabras = ['Sustantivo','Verbo', 'Adjetivo']
    diccionario_palabras = {'verbo':[], 'sustantivo':[], 'adjetivo':[]}
    if event is None:
        break
    else:
        if(event in 'Verbo'):
            print(event)
            tipo_palabra = event
            ventana.Element('_NOUN_').Update(disabled=True)[False]
            #        window.Element('_B_').Update(('CAMBIO ON','On')[down], button_color=(('white', ('red', 'green')[down])))

        if(event in abecedario):
            value = event
            print(value)


            # while flag:
            #     value = event
            #     palabra = palabra + value
            #     if( event == 'OK'):
            #         flag = False
            #         duccionario[tipo_palabra].append(palabra)
            # print(palabra)





ventana.Close()


# import PySimpleGUI as sg
#
#
# layout = [[sg.Text('A toggle button example')],
#           [sg.Button('On', size=(3,1), button_color=('white', 'green'), key='_B_'), sg.Button('Exit')]]
#
# window = sg.Window('Toggle Button Example', layout)
#
# down = True
#
# while True:             # Event Loop
#     event, values = window.Read()
#     if event in (None, 'Exit'):
#         break
#     elif event == '_B_':
#         down = not down
#         window.Element('_B_').Update(('CAMBIO ON','On')[down], button_color=(('white', ('red', 'green')[down])))
#
# window.Close()
